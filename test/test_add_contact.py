# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev", company="issart", address="omsk", email="dmatveev@issart.com"))
    app.session.logout()