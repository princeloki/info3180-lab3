#For some reason the code does not run unless you explicitly specify the absolute path that contains the forms module
import sys
sys.path.append("C:/Users/teriq/OneDrive/Documents/Return to coding/INFO3180/info3180-lab3/app")

from forms import ContactForm
from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
from app import views

