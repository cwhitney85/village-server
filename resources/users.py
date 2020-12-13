import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

# Define Users Blueprint
user = Blueprint('users', __name__, url_prefix='/user')

# Register a new user
@user.route('/register', methods=["POST"])
def register():
  payload = request.get_json()

  payload['email'] = payload['email'].lower()
  try:
    # Check if user exists
    models.Users.get(models.Users.email == payload['email'])
    return jsonify(data={}, status={"code": 401, "message": "A user with that name already exists"})
  except models.DoesNotExist:
    # If user does not exist, create a new  one
    payload['password'] =  generate_password_hash(payload['password'])
    user = models.Users.create(**payload)

    # Then log them in
    login_user(user)

    user_dict = model_to_dict(user)
    print(user_dict)
    print(type(user_dict))
    del user_dict['password']

    return jsonify(data=user_dict, status={"code": 201, "message": "Success"})