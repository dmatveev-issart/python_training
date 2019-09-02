# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev", company="issart", address="omsk", email="dmatveev@issart.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    sleep(1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
