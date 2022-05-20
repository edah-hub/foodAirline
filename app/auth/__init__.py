from flask import Blueprint
auth = Blueprint('auth',__name__)  # blueprint instance
from . import views, forms
