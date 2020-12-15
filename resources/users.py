import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
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


# Login an existing user
@user.route('/login', methods=["POST"])
def login():
  payload = request.get_json()
  print('payload:', payload)
  payload['email'] = payload['email'].lower()
  try:
    user = models.Users.get(models.Users.email == payload['email'])
    user_dict = model_to_dict(user)
    if (check_password_hash(user_dict['password'], payload['password'])):
      del user_dict['password']
      login_user(user)
      print(user, ' this is current user')
      return jsonify(data=user_dict, status={"code": 200, "message": "Successful login!"})
    else:
      return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "User does not exist"})

@user.route('/', methods=["GET"])
def getUsers():
  try:
    users = [model_to_dict(user) for user in models.Users.select()]
    print(users)
    return jsonify(data=users, status={"code": 200, "message": "Here are the users"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "Failed to retrieve the users"})


# End a session by logging out
@user.route('/logout', methods=["GET"])
def logout():
  logout_user()
  return jsonify(data={}, status={"code": 200, "message": "Successful logout!"})
