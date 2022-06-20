from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (LoginManager,UserMixin,login_user,login_required,
logout_user,current_user)
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/bandar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
CORS(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'UserView:login'

# In models directory there is a models file from which all the models are imported
from application.models.models import *

from application.views.UserView import UserView
from application.views.HomeView import HomeView
from application.views.AdminView import AdminView

UserView.register(app)
HomeView.register(app)
AdminView.register(app)