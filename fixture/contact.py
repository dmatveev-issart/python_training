# -*- coding: utf-8 -*-


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        self.open_add_new_page()
        # fill contact form
        self.app.fill_text_field("firstname", contact.firstname)
        self.app.fill_text_field("middlename", contact.middlename)
        self.app.fill_text_field("lastname", contact.lastname)
        self.app.fill_text_field("nickname", contact.nickname)
        self.app.fill_text_field("company", contact.company)
        self.app.fill_text_field("address", contact.address)
        self.app.fill_text_field("email", contact.email)
        self.submit_contact_creation()
        self.return_to_home_page()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def modify(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # click pencil icon
        self.click_edit()
        # fill contact form
        self.app.fill_text_field("firstname", contact.firstname)
        self.app.fill_text_field("middlename", contact.middlename)
        self.app.fill_text_field("lastname", contact.lastname)
        self.app.fill_text_field("nickname", contact.nickname)
        self.app.fill_text_field("company", contact.company)
        self.app.fill_text_field("address", contact.address)
        self.app.fill_text_field("email", contact.email)
        # click update button
        self.click_update()
        self.app.open_home_page()

    def click_update(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()

    def click_edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit pop-up confirmation window
        wd.switch_to_alert().accept()
        self.app.open_home_page()



