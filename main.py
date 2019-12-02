import sys
from datetime import date
from peewee import *
print('hello world')

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)


class Basemodel(Model):
    class Meta:
        database = db


class Contact(Basemodel):
    name = CharField()
    birthday = DateField()
    number = CharField()


db.connect()
db.create_tables([Contact])

contact_prompt = input("would you like to create a new contact y/n")
if contact_prompt == "y":
    name_prompt = input("name")
    name
