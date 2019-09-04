# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev", company="issart", address="omsk", email="dmatveev@issart.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    sleep(1)
    assert len(old_contacts) - 1 == (app.contact.count())
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
