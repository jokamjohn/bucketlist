from flask import Flask

# Initialize the application
app = Flask(__name__, instance_relative_config=True)

# App configs
app.secret_key = 'nbvjlisghruvnxzdnvdlsfgvbfugfvbjsdkvbusdigkbsdjkval'
app.config['SESSION_TYPE'] = "filesystem"

# Load the views
from app import views

# Linking the configuration file
app.config.from_object('config.BaseConfig')
