# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep
import random


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev",
                                   company="issart", address="omsk", email="dmatveev@issart.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    app.contact.delete_contact_by_id(contact.id)
    sleep(1)
    new_contacts = db.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
