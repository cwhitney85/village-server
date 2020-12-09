from peewee import *
import datetime

DATABASE = PostgresqlDatabase('village')


# Cook model for producers
class Cooks(Model):
  name = CharField()
  specialty = CharField()
  location = CharField()

  class Meta:
    database = DATABASE


# Initialize tables
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Cooks], safe=True)
  print("TABLES Created")
  DATABASE.close()