import datetime
from peewee import *
from flask_login import UserMixin

DATABASE = PostgresqlDatabase('village')

# Users model
class Users(UserMixin, Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField(unique=True)
  password = CharField()
  address = CharField()

  class Meta:
    database = DATABASE

# Cook model for producers - every cook is a user... not every user is a cook
class Cooks(Model):
  username = CharField(unique=True)
  specialty = CharField()
  user_location = CharField(ForeignKeyField(Users.address, backref='location'))
  avatar = CharField(default='https://tfnbk-bank.com/wp-content/uploads/2018/10/avatar.png')
  banner = CharField()

  user = ForeignKeyField(Users, backref='cook')

  class Meta:
    database = DATABASE

# Meal model with one to many relationship to cook
class Meals(Model):
  cuisine = CharField()
  price = FloatField()
  units = IntegerField()
  recipe = TextField()
  image = CharField()
  cook_location = ForeignKeyField(Cooks.user_location, backref='hub')

  cook = ForeignKeyField(Cooks, backref='meal')

  class Meta:
    database = DATABASE


# Initialize tables
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Users, Cooks, Meals], safe=True)
  print("TABLES Created")
  DATABASE.close()