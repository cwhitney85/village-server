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
  avatar = CharField()
  banner = CharField()

  user = ForeignKeyField(Users, backref='cook', primary_key=True)

  class Meta:
    database = DATABASE

# Meal model with one to many relationship to cook
class Meals(Model):
  name = CharField()
  cuisine = CharField()
  price = FloatField()
  units = IntegerField()
  recipe = TextField()
  image = CharField()

  cook = ForeignKeyField(Cooks, backref='meal')

  class Meta:
    database = DATABASE


# Initialize tables
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Users, Cooks, Meals], safe=True)
  print("TABLES Created")
  DATABASE.close()