# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="modified_name", header="modified_header", footer="modified_footer"))
    app.session.logout()