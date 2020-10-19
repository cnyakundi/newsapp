from flask import Flask

from .config import DevConfig

# Initializing our application
app = Flask(__name__)

# Production configuration

app.config.from_object(DevConfig)


from app import views
