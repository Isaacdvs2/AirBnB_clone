#!/usr/bin/python3

import cmd

""" The console program for the project """

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
