# -*- coding: utf-8 -*-


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    print("contact_from_home_page = {}".format(contact_from_home_page))
    print("contact_from_edit_page = {}".format(contact_from_edit_page))
