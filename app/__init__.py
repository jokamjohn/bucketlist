from flask import Flask
from flask_login import LoginManager

# Initialize the application
app = Flask(__name__, instance_relative_config=True)

# Initialize login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

# App configs
app.secret_key = 'nbvjlisghruvnxzdnvdlsfgvbfugfvbjsdkvbusdigkbsdjkval'
app.config['SESSION_TYPE'] = "filesystem"

# Load the views
from app import views

# Linking the configuration file
app.config.from_object('config.BaseConfig')
