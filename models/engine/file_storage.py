#!/usr/bin/python3
"""FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes inst to JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format
                              (obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dictionary = {}
        for key, obj in FileStorage.__objects.items():
            dictionary[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary, f)

    def reload(self):
        """Deserializes the JSON file"""
        try:
            with open(FileStorage.__file_path) as f:
                dictionary = json.load(f)
                for obj in dictionary.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
