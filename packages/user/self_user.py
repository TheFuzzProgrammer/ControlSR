# Created by fuzz at 26/4/19
"""This compilation / file uses a Open Source licence, most of developers,
in a part of their lives, uses some software that have it too, so, as you
know, you are part of that developers, from the Open Source community 
we have loved of that, and it will great to someday we can use some contribution from you
from you, thanks for be part of this"""


class user_admin():
    def __init__(self, name, surname, id, photo):

        self.user_name = name
        self.user_surname = surname
        self.user_id = id
        self.user_photo = photo
        """Must be the location of pic"""
        self.privations = False
        self.rol = 'admin'


class new_user():
    def __init__(self, name, surname, id, photo):

        self.user_name = name
        self.user_surname = surname
        self.user_id = id
        self.user_photo = photo
        """Must be the location of pic"""
        self.privations = True


if __name__ == '__main__':

    print('Should not run this')
