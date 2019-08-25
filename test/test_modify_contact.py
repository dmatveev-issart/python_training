# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_contact(app):
    app.contact.modify_first_contact(Contact(firstname="eugene", middlename="pavlovich", lastname="denisov", nickname="edenisov", company="mostovik", address="Novosibirsk", email="edenisov@mostovik.ru"))
