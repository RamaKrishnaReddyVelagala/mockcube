from flask import Flask
from markupsafe import escape

app = Flask(__name__)

from app.routes.arithmetic_ops import *  # Import routes
