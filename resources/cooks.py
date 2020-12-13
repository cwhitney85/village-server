import models

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from playhouse.shortcuts import model_to_dict


cook = Blueprint('cooks', __name__, url_prefix='/api/v1/cooks')

@cook.route('/')
@login_required
def index():
  return "This is a cooking app for some reason"