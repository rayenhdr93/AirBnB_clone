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

    def do_update(self, line):
        models.storage.reload()
        list = line.split()
        if len(list) == 0:
            print("** class name missing **")
        else:
            if list[0] not in classes:
                print("** class doesn't exist **")
            elif list[0] in classes:
                if len(list) == 1:
                    print("** instance id missing **")
                    return False
                key = "{}.{}".format(list[0], list[1])
                if key in models.storage.all():
                    dict_to_update = models.storage.all()[key].__dict__
                    if len(list) == 2:
                        print("** attribute name missing **")
                    elif len(list) == 3:
                        print("** value missing **")
                    else:
                        k = list[2]
                        try:
                            attrtype = type(dict_to_update[k])
                            v = attrtype(list[3])
                        except KeyError:
                            v = list[3]
                        dict_to_update[k] = v
                        models.storage.save()
                else:
                    print("** no instance found **")

    def do_count(self, line):
        list = line.split()
        counter = 0
        for key, value in models.storage.all().items():
            if key.split(".")[0] == list[0]:
                counter += 1
        print(counter)

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program\n")

    def default(self, line):
        list = line.split(".")
        if len(list) > 1 and list[0] in classes:
            print("hello")
            if list[1] == "all()":
                return self.do_all(list[0])
            elif list[1] == "count()":
                return self.do_count(list[0])
            else:
                replace_list = list[1].replace(
                    "(", " ").replace(
                    ")", "").replace(
                    ",", "")
                new_list = replace_list.split()
                Cname_id = "{} {}".format(list[0], new_list[1])
                print(Cname_id)
                print(len(new_list))
                print(new_list)
                if new_list[0] == "show":
                    return self.do_show(Cname_id)
                elif new_list[0] == "destroy":
                    return self.do_destroy(Cname_id)
                elif new_list[0] == "update":
                    if len(new_list) == 4:
                        Cname_id += " " + new_list[2] + " " + new_list[3]
                        return self.do_update(Cname_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
