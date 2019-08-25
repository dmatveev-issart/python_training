# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_contact(app):
    app.contact.modify_first_contact(Contact(firstname="eugene", middlename="pavlovich", lastname="denisov", nickname="edenisov", company="mostovik", address="Novosibirsk", email="edenisov@mostovik.ru"))


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New lastname"))