#!/usr/bin/python3
""" Entry point of the interpreter """
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ cmd & parameters class """
    modelos = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]
    if sys.stdin.isatty():
        prompt = '(hbnb)'
    else:
        prompt = '(hbnb)\n'

    def Main_menu():
        """ principal function """
        do_EOF(self, arg)
        do_quit(self, arg)
        emptyline(self)

    def defecto(self, arg):
        if '.' not in arg:
            print("*** Unknown syntax: ", arg)
            return

    x = arg.split('.')
    if x[0]=="":
        print("** class name missing **")
    if x[0] not in HBNBCommand.modelos:
        print("** class doesn't exist **")
    if x[1]=="all()":
        self._all(x[0])
    elif x[1]=="count()":
        self._count(x[0])
    elif x[1][0:5] == "show(" and x[1][-1] == ")":
        self._show(x[0], x[1])
    elif x[1][0:8] == "destroy(" and x[1][-1] == ")":
        self._destroy(x[0], x[1])
    elif x[1][0:7] == "update(" and x[1][-1] == ")":
        self._update(x[0], x[1])
    else:
        print("*** Unknown syntax: ", arg)
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
