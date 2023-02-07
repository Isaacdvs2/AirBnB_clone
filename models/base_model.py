#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
"""
The BaseModel class defines the common attributes/methods for other classes.

Public instance attributes:
	- id : string - assign with an uuid when an instance is created. The
	        uuid must be unique for every instance.
	- created_at: datetime - assign with the current datetime when an instace
                is created.
	- updated_at: datetime - assign with the current datetime when an instance 
                is created and it will be updated every time you change your object.

Public instance methods: save(), to_dict()
"""

    def __init__(self, *args, **kwargs):
        """
         The init method is the constructor for the base model
        """
        self.id = str(uuid4())
	self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the string representation of the base model object in the form:
           [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(self.__name__, self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
	self.updated_at = datetime.now()
        storage.save()
        return 0
    def to_dict(self):
        return 0
        return 0
