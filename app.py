from flask import Flask, jsonify, g

import models

DEBUG = True
PORT = 8000

# Initialize the Flask class instance
app = Flask(__name__)

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
  return 'Let\'s get cookin\''

# Start the app and create tables
if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)
