from flask import Flask

from .config import DevConfig

from flask_bootstrap import Bootstrap

# Initializing our application
app = Flask(__name__, instance_relative_config=True)

# Production configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
