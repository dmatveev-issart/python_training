# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, json_groups, db, check_ui):
    group_data = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test group", header="Test header", footer="Test footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    app.group.modify_group_by_id(group.id, group_data)
    new_groups = db.get_group_list()
    old_groups[index] = new_groups[index]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




