import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import path
from flask_socketio import SocketIO









app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'




db = SQLAlchemy(app)
socketio = SocketIO()


bcrypt = Bcrypt(app)


admin = Admin(app)




login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)
socketio.init_app(app, async_mode='eventlet')


from elturino import routes
from . import models
admin.add_view(models.SecureModelView(models.Post, db.session))

from .models import User

if not path.exists('elturino/site.db'):
        db.create_all(app=app)
        print('created')


