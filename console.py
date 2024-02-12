import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNB Command Interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Goodbye!")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) != 1:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
        except:
            print("** class doesn't exist **")
            return
        if not issubclass(cls, BaseModel):
            print("** class doesn't exist **")
            return
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) > 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) > 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        if arg:
            try:
                cls = eval(arg)
            except:
                print("** class doesn't exist **")
                return
            if not issubclass(cls, BaseModel):
                print("** class doesn't exist **")
                return
            print([str(val) for key, val in storage.all().items() if key.startswith(arg)])
        else:
            print([str(val) for key, val in storage.all().items()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = arg.split()
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) > 4:
            print("** attribute name missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if args[3][0] != '"' or args[3][-1] != '"':
            print("** value missing **")
            return
        args[3] = args[3][1:-1]
        setattr(storage.all()[key], args[2], args[3])
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
