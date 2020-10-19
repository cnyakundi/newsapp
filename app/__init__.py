from flask import Flask

from .config import DevConfig

# Initializing our application
app = Flask(__name__, instance_relative_config=True)

# Production configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
