#!/usr/bin/python3
"""Interpretator"""
import cmd
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.base_model import BaseModel
from models import storage

classes = {
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "User": User,
        "BaseModel": BaseModel 
        }

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the program."""
        exit()

    def do_EOF(self, arg):
        """Quit the program."""
        exit()

    def do_create(self, arg=""):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg=""):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            for k, v in storage.all().items():
                if k == key and v.id == args[1]:
                    print(v)
                    break
            else:
                print("** no instance found **")

    def do_destroy(self, arg=""):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        if not arg or arg in classes:
            print([str(obj) for obj in storage.all().values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg=""):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()

    def emptyline(self):
        """Catches enter"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
