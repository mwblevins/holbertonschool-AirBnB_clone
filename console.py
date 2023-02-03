#!/usr/bin/python3
"""Creates Console module for Airbnb Clone"""


import cmd
from models.base_model import *
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    supported_classes = ["BaseModel", "User", "State",
                         "City", "Amenity", "Place", "Review"]

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
            print("** class dosent exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all().keys():
            print("** no instance found **")
        storage.remove(key)
        storage.save()
        return
    
        
            
        
            
                
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
