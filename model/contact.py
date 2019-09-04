# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname and self.lastname == other.lastname)

    def id_or_max(cr):
        if cr.id:
            return int(cr.id)
        else:
            return maxsize
