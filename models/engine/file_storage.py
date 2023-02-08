#!/usr/bin/python3

import json

"""
The storage module for saving objects and progress in the program
"""

class FileStorage:
    """
    The FileStorage class is class to ensure all objects createdby our
    program are saved. This will make our program to restore all objects created
    before when our program is launched. The class also  serializes instances to a JSON 
    file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serialises the __objects to the JSON file i.e file.json """
        with open(self.__file_path, mode = "w") as f:
            py_dict = {}
            for key, value in self.__objects.items():
                py_dict[key] = value.to_dict()
            json.dump(py_dict, f)
