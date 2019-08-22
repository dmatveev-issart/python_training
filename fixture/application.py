# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def fill_text_field(self, text_field_name, text_field_value):
        wd = self.wd
        wd.find_element_by_name(text_field_name).click()
        wd.find_element_by_name(text_field_name).clear()
        wd.find_element_by_name(text_field_name).send_keys(text_field_value)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")