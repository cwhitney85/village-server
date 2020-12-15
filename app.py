from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager

DEBUG = True
PORT = 8000

import models
from resources.cooks import cook
from resources.users import user

login_manager = LoginManager()

# Initialize the Flask class instance
app = Flask(__name__)

# Set up secret key and initiate sessions
app.secret_key = "BABYWYATT"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
  try:
    return models.Users.get(models.Users.id == userid)
  except models.DoesNotExist:
    return None

# Access database globally and connect before each request
@app.before_request
def before_request():
  g.db = models.DATABASE
  g.db.connect()

# Close database connection after each request
@app.after_request
def after_request(response):
  g.db.close()
  return response

# Default Index Route
@app.route('/')
def index():
  return "<h1>Let's Get Cookin'</h1>"

CORS(cook, origins=['*'], supports_credentials=True)
app.register_blueprint(cook)

CORS(user, origins=['*'], supports_credentials=True)
app.register_blueprint(user)

# Start the app and create tables
if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)
