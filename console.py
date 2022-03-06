#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line == "BaseModel":
            new_ins = BaseModel()
            new_ins.save()
            print(new_ins.id)
        elif line == "User":
            new_ins = User()
            new_ins.save()
            print(new_ins.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        else:

            if list[0] not in ("BaseModel", "User"):
                print("** class doesn't exist **")
            elif len(list) < 2:
                print("** instance id missing **")
            else:
                ids = storage.all()
                if (list[0] + "." + list[1]) in ids.keys():
                    print(ids[list[0] + "." + list[1]])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        else:
            if list[0] not in ("BaseModel", "User"):
                print("** class doesn't exist **")
            elif len(list) < 2:
                print("** instance id missing **")
            else:
                ids = storage.all()
                if ids[list[0] + "." + list[1]]:
                    del(ids[list[0] + "." + list[1]])
                    storage.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
