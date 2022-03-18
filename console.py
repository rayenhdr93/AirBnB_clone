#!/usr/bin/python3
""" HBNBCommand """
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Simple command processor"""

    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program\n")
 
    def do_create(self, line):
        list = line.split()
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] in classes:
            new_in = classes[list[0]]()
            print(new_in.id)
            new_in.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        list = line.split()
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] in classes:
            if len(list) == 2:
                key = "{}.{}".format(list[0], list[1])
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        list = line.split()
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] in classes:
            if len(list) == 2:
                key = "{}.{}".format(list[0], list[1])
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        list = line.split()
        if len(list) > 0 and list[0] not in classes:
            print("** class doesn't exist **")
        else:
            string_list = []
            for value in models.storage.all().values():
                if len(list) > 0 and list[0] == value.__class__.__name__:
                    string_list.append(value.__str__())
                elif len(list) == 0:
                    string_list.append(value.__str__())
            print(string_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
