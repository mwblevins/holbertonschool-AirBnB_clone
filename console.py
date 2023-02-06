#!/usr/bin/python3
"""Creates Console module for Airbnb Clone"""


import cmd
from models.base_model import *
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    supported_classes = ["BaseModel", "User", "State",
                         "City", "Amenity", "Place", "Review"]

    blackList = ["id", "created_at", "updated_at"]
    
    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit on EOF"""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass
    
    def do_create(self, line):
        """Creates a neew instance of BaseModel, saves and prints id"""
        if not line:
            print("** class name missing **")
        else:
            try:
                cls = eval(line)()
                cls.save()
                print(cls.id)
            except (NameError, AttributeError):
                print('** class doesnt exist **')

    def do_show(self, line):
        """prints the string represenation of an instance based on the class name/id"""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return  
        class_name, instance_id = args[0], args[1]
        if class_name not in HBNBCommand.supported_classes:
            print("** class dosent exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        res = storage.all().get(key) or ("** no instance found **")
        print(res)

    def do_destroy(self, line):
        """Deletes and instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return  
        class_name, instance_id = args[0], args[1]
        if class_name not in HBNBCommand.supported_classes:
            print("** class doesnt exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all().keys():
            print("** no instance found **")
        storage.remove(key)
        storage.save()
        return
    
    def do_all(self, line):
        """Prints all string represenation of all instances based or not on the class name"""
        if line == "":
            print([str(i) for i in storage.all().values()])
            return
        
        if line in HBNBCommand.supported_classes:
            print([str(i) for k, i in storage.all().items() if line in k])
        else:
            print("** class doesnt exist **")
        
    def do_update(self, line):
        """Udates an instance based on the class name and id"""
        errMsgs = ["class name missing", "instance id missing",
                   "attribute name missing", "value missing"]
        args = line.split()
        if len(args) < 4:
            print("** {} **".format(errMsgs[len(args)]))
            return
        if args[0] not in HBNBCommand.supported_classes:
            print("** class doesnt exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        target = storage.all().get(key)
        if target is None:
            print("** no instance found **")
            return
        if args[2] in HBNBCommand.blackList:
            return
        setattr(target, args[2], eval(args[3]))
            
         


if __name__ == '__main__':
    HBNBCommand().cmdloop()
