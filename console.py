#!/usr/bin/python3
"""
program that contains the entry point of the command interpreter
"""

import cmd
import models
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This class to setup the command interpreter """
    my_class = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Exit the CMD program'''
        return True

    def do_EOF(self, line):
        '''Exit the CMD program'''
        return True

    def emptyline(self):
        '''Do nothing'''
        pass

    def do_create(self, line):
        '''Creates a new instance of BaseModel'''
        _line = line.split()

        if line == "":
            print("** class name missing **")
            return False
        elif _line[0] not in self.my_class:
            print("** class doesn't exist **")
        else:
            nw_inst = self.my_class[_line[0]]()
            print(nw_inst.id)
            nw_inst.save()

    def do_show(self, line):
        '''Prints the string representation
        of an instance based on the class name and id'''
        if (type(line) == str):
            _line = line.split()
            ln_arg = len(_line)

            if (self.check_if_created(_line, ln_arg) != 1):

                obt_inst = _line[0] + "." + _line[1]
                d_class= models.storage.all()

                if obt_inst in d_class.keys():
                    print(d_class[obt_inst])
                else:
                    print("** no instance found **")
        else:
            _id = line[0] + "." + line[1]
            d_class = models.storage.all()
            if _id in d_class.keys():
                print(d_class[_id])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class
        name and id (save the change into the JSON file).'''
        _line = line.split()
        ln_arg = len(_line)
        if (self.check_if_created(_line, ln_arg) != 1):

            obt_inst = _line[0] + "." + _line[1]
            dic_class = models.storage.all()

            if obt_inst in d_class.keys():
                del d_class[obt_inst]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        '''Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all.'''
        _line = line.split()
        if line == "" or _line[0] in self.my_class:
            d_class = models.storage.all()
            ls_class = []
            for key, value in d_class.items():
                if line in key:
                    ls_class.append(value.__str__())
            print(ls_class)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@holbertonschool.com".'''
        _line = line.split()
        ln_arg = len(_line)

        if (self.check_if_created(_line, ln_arg) == 1):
            pass
        elif (ln_arg == 2):
            print("** attribute name missing **")
        elif (len_args == 3):
            print("** value missing **")
        else:
            obt_inst = _line[0] + "." + _line[1]
            d_class = models.storage.all()
            if obt_inst in d_class.keys():
                if _line[3]:
                    _line[3] = _line[3].replace('"', "")
                try:
                    _line[3] = int(_line[3])
                except ValueError:
                    try:
                        _line[3] = float(_line[3])
                    except ValueError:
                        _line[3] = _line[3]
                d_class[obt_inst].__dict__[_line[2]] = _line[3]
                d_class[obt_inst].save()
            else:
                print("** no instance found **")

    def default(self, line):
        '''Get's all method names that aren't defined'''
        _line = line.split('.')
        if len(_line) > 1:
            if _line[1] == "all()":
                self.do_all(_line[0])
            if _line[1] == "count()":
                self.do_count(_line[0])

            my_count = _line[1].split('"')
            res = re.findall(r'\(.*?\)', _line[1])
            my_count[0] = my_count[0] + line[-1]
            if my_count[0] == "show()":
                myNewList = [_line[0], my_count[1]]
                self.do_show(myNewList)
        else:
            cmd.Cmd.default(self, line)

    def check_if_created(self, _line, ln_arg):
        '''Verifies if the class exists'''
        if ln_arg == 0:
            print("** class name missing **")
            return 1
        elif _line[0] not in self.my_class:
            print("** class doesn't exist **")
            return 1
        elif (ln_arg == 1):
            print("** instance id missing **")
            return 1

    def do_count(self, line):
        '''Counts and retrive the number of existing instances'''
        _line = line.split()
        if line == "" or _line[0] in self.my_class:
            d_class = models.storage.all()
            ls_class = []
            count = 0
            for key, value in d_class.items():
                if line in key:
                    ls_class.append(value.__str__())
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
