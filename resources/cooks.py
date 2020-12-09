import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict


cook = Blueprint('cooks', __name__, url_prefix='/api/v1/cooks')

@cook.route('/')
def index():
  return "This is a cooking app for some reason"