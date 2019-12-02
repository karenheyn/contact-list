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


def create_contact():
    contact_prompt = str(input("would you like to create a new contact y/n "))
    if contact_prompt == "y":
        name_prompt = str(input("name "))
        year = int(input("what year were they born? "))
        month = int(input("what month were they born? "))
        day = int(input("what day were they born? "))
        number_prompt = str(input("phone number "))
        new_contact = Contact(name=name_prompt, birthday=date(
            year, month, day), number=number_prompt)
        new_contact.save()
        create_contact()
    list_prompt = str(input("would you like to view all contacts y/n "))
    if list_prompt == "y":
        list_all()
    search_prompt = str(
        input("would you like search contacts y/n "))
    if search_prompt == "y":
        search()
    else:
        print("goodbye")
        sys.exit()


def list_all():
    for contact in Contact.select():
        print(f"{contact.name}\n{contact.birthday}\n{contact.number}\n\n")


def search():
    search_prompt = str(input("who would you like to search for? "))
    searched = Contact.select().where(Contact.name.contains(search_prompt)).get()
    print(f"{searched.name}\n{searched.birthday}\n{searched.number}")


create_contact()
