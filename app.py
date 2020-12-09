from flask import Flask, jsonify

DEBUG = True
PORT = 8000

# Initialize the Flask class instance
app = Flask(__name__)

# Default Index Route
@app.route('/')
def index():
  return 'Let\'s get cookin\''

# @app.route('/json')
# def cook():
#   return jsonify(name="Colin", speciality="Grill Master", todays_meal="Bone-in Ribeye")

# Start the app
if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)
