# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev", company="issart", address="omsk", email="dmatveev@issart.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="eugene", middlename="pavlovich", lastname="denisov", nickname="edenisov", company="mostovik", address="Novosibirsk", email="edenisov@mostovik.ru")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == (app.contact.count())
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


"""def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev", company="issart", address="omsk", email="dmatveev@issart.com"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev", company="issart", address="omsk", email="dmatveev@issart.com"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))"""