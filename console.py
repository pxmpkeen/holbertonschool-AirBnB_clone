#!/usr/bin/python3
"""Interpretator"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the program."""
        exit()

    def do_EOF(self, arg):
        """Quit the program."""
        exit()

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 1:
            print("** class name missing **")
        elif len(args) == 2:
            print("** instance id missing **")


    def do_destroy(self, arg):


    def emptyline(self):
        """Catches enter"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
