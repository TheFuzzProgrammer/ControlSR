# Created by fuzz at 26/4/19
"""This compilation / file uses a Open Source licence, most of developers,
in a part of their lives, uses some software that have it too, so, as you
know, you are part of that developers, from the Open Source community 
we have loved of that, and it will great to someday we can use some contribution from you
from you, thanks for be part of this"""

import pickle
import os

class languaje():
    def __init__(self, name):
        self.languaje_name = name
        self.main_ui_lang = list()
        self.setup_ui_lang = list()
        set_lang = True
        while set_lang:
            print('For what UI you wanna write?')
            what_ui_lang = input('a = Main b = settings c= cancel d = WRITE SUCESFULL')
            while what_ui_lang == 'a':
                print('writting languaje for main window')
                try:
                    word = input()
                    self.main_ui_lang.append(word)
                    print('Stay with task? Y/N')
                    word = input()
                    if word is 'y' or word is 'Y':
                        pass
                    else:
                        what_ui_lang = 'b'
                except:
                    set_lang = False

            while what_ui_lang == 'b':
                print('writting languaje for settings window')
                try:
                    word = input()
                    self.setup_ui_lang.append(word)
                    print('Stay with task? Y/N')
                    word = input()
                    if word is 'y' or word is 'Y':
                        pass
                    else:
                        what_ui_lang = 'kill_task'
                        set_lang = False

                except:
                    set_lang = False
            if what_ui_lang == 'c' or what_ui_lang is 'C':
                self.languaje_name = 'aborted'
                break

def new_lang_write(lang_name):
        if not os.path.exists('../../binary/lang.dat'):
            open('../../binary/lang.dat', 'w')

        try:
            print(os.getcwd().replace('/packages/user', '/binary/lang.dat'), os.getcwd())
            write_to = '../../binary/lang.dat'
            file = open(write_to, 'ab')
            pickle.dump(lang_name, file)

        except:
            pass



def new_lang_create(name):
    new_lang = languaje(name)
    if new_lang.languaje_name is not 'aborted':
        new_lang_write(new_lang)
        return 0
    else:
        pass
        return new_lang.languaje_name


if __name__ == "__main__" :
    print(os.getcwd().replace('/packages/user', '/binary/lang.dat'), os.getcwd())
    new_lang_create(input('name of new lang'))

