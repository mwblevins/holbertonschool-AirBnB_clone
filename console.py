#!/usr/bin/python3
"""Creates Console module for Airbnb Clone"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit on EOF"""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
