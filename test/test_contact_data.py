# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import re


def test_some_contact_data(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="denis", middlename="sergeevich", lastname="matveev", nickname="dmatveev", company="issart", address="omsk", email="dmatveev@issart.com"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear_phones(s):
    return re.sub("[() -]", "", s)


def clear_email(s):
        return s


def merge_emails_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear_email(x),
                                    filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
