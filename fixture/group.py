# -*- coding: utf-8 -*-


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.click_new_group()
        # fill group form
        self.app.fill_text_field("group_name", group.name)
        self.app.fill_text_field("group_header", group.header)
        self.app.fill_text_field("group_footer", group.footer)
        # submit group creation
        self.click_enter_information()
        self.return_to_groups_page()

    def click_enter_information(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def click_new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def modify(self, group):
        self.open_groups_page()
        self.click_first_group()
        self.click_edit_group()
        # fill group form
        self.app.fill_text_field("group_name", group.name)
        self.app.fill_text_field("group_header", group.header)
        self.app.fill_text_field("group_footer", group.footer)
        # submit group modification
        self.click_update()
        self.return_to_groups_page()

    def click_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def click_edit_group(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def click_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.click_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()