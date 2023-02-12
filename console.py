#!/usr/bin/python3

import cmd

""" The console program for the project """

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

def check_args(args):
    """checks if args is valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list

class HBNBCommand(cmd.Cmd):

    """
    the class that implements the console for the project
    """

    prompt = "(hbnb)"

    def do_quit(self, argv):
        """ handles the functionality to exit a program """
        return True

    def do_EOF(self, argv):
        """ handles exiting of the program when EOF signal is recieved """
        print("")
        return True

    def do_create(self, argv):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
         and prints the id"""
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
