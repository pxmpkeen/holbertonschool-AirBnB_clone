#!/usr/bin/python3
"""Interpretator"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, str):
        """Quit the program."""
        exit()

    def do_EOF(self, str):
        """Quit the program."""
        exit()

    def emptyline(self):
        """Catches enter"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
