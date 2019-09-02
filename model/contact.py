# -*- coding: utf-8 -*-


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None, email=None, id=None, name=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.email = email
        self.id = id
        self.name = name

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
