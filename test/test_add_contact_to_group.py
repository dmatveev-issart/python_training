# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_add_contact_to_group(app, db):
    contacts_list = db.get_contact_list()
    index = len(contacts_list)
    contact = random.choice(contacts_list)
    app.contact.add_contact_to_group_by_id(contact.id)
    #print("added = ", db.get_contact_in_group_list())
    assert db.get_contact_in_group_list().count(contact.id) == 1