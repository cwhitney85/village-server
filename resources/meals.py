import models

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from playhouse.shortcuts import model_to_dict


meal = Blueprint('meals', __name__, url_prefix="/api/v1/meals")


# Get all meals
@meal.route('/', methods=["GET"])
def get_all_meals():
  try:
    meals = [model_to_dict(meals) for meals in models.Meals.select()]
    return jsonify (data=meals, status={"code": 200, "message": "Success"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

# Create a Meal
@meal.route('/<cookid>', methods=["POST"])
def create_meal(cookid):
  cook = models.Cooks.get_by_id(cookid)
  payload = request.get_json()
  print(payload)
  print(cook)
  new_meal = models.Meals.create(name=payload['name'], cuisine=payload['cuisine'], price=payload['price'], units=payload['units'], recipe=payload['recipe'], image=payload['image'], cook_location=cook.user_location, cook=cook.user_id)
  meal_dict = model_to_dict(new_meal)
  return jsonify(data=meal_dict, status={"code": 200, "message": "Meal created"})