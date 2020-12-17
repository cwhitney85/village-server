import models

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from playhouse.shortcuts import model_to_dict


cook = Blueprint('cooks', __name__, url_prefix='/api/v1/cooks')

@cook.route('/test', methods=["GET"])
@login_required
def index():
  return "This is a cooking app for some reason"


# Route to return users cook
@cook.route('/', methods=["GET"])
@login_required
def get_my_cook():
  try:
    cook = [model_to_dict(cook) for cook in current_user.cook]
    print(cook)
    return jsonify(data=cook, status={"code": 200, "message": "Success, here's your cook"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "Error getting your cook"})


# Get a cook by id
@cook.route('/', methods=["GET"])
def get_some_cook(cookid):
  try:
    cook = models.Cooks.get_by_id(cookid)
    cook_dict = model_to_dict(cook)
    return jsonify(data={cook_dict}, status={"code": 200, "message": "Success, have a look at your cook"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "Cook not found"})

# Create a cook
@cook.route('/', methods=["POST"])
def create_cook():
  payload = request.get_json()
  print(payload)

  new_cook = models.Cooks.create(username=payload['username'], specialty=payload['specialty'], user_location=current_user.address, avatar=payload['avatar'], banner=payload['banner'], user=current_user.id)
  cook_dict = model_to_dict(new_cook)
  return jsonify(data=cook_dict, status={"code": 200, "message": "Cook Created"})