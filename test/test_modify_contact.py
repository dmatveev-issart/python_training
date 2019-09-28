# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_mod_contact(app, db, json_contacts, check_ui):
    contact_data = json_contacts
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev",
                                   company="issart", address="omsk", email="dmatveev@issart.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    app.contact.modify_contact_by_id(contact.id, contact_data)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contacts[index]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
