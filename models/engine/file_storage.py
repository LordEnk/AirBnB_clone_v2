#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os
from importlib import import_module


class FileStorage:
	"""Class for storing and retrieving data"""
	__file_path = "file.json"
	__objects = {}

	def __init__(self):
		"""Initializes a FileStorage instance"""
		self.model_classes = {'BaseModel': import_module('models.base_model').BaseModel,'User': import_module('models.user').User, 'State': import_module('models.state').State, 'City': import_module('models.city').City, 'Amenity': import_module('models.amenity').Amenity, 'Place': import_module('models.place').Place, 'Review': import_module('models.review').Review}

	def all(self, cls=None):
		"""Returns a dictionary of models currently in storage"""
		if cls is None:
			return self.__objects
		else:
			filtered_dict = {}
		for key, value in self.__objects.items():
			if type(value) is cls:
				filtered_dict[key] = value
		return filtered_dict
	def delete(self, obj=None):
		"""Removes an object from the storage dictionary"""
		if obj is not None:
			obj_key = obj.to_dict()['__class__'] + '.' + obj.id
		if obj_key in self.__objects.keys():
		del self.__objects[obj_key

	def new(self, obj):
		"""sets in __objects the obj with key <obj class name>.id"""
		key = "{}.{}".format(type(obj).__name__, obj.id)
		FileStorage.__objects[key] = obj

	def save(self):
		""" serializes __objects to the JSON file (path: __file_path)"""
		with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
			d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
			json.dump(d, f)

	def classes(self):
		"""Returns a dictionary of valid classes and their references"""
		from models.base_model import BaseModel
		from models.user import User
		from models.state import State
		from models.city import City
		from models.amenity import Amenity
		from models.place import Place
		from models.review import Review
		
		classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}
		return classes

	def reload(self):
		"""Reloads the stored objects"""
		if not os.path.isfile(FileStorage.__file_path):
			return
		with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
			obj_dict = json.load(f)
			obj_dict = {k: self.classes()[v["__class__"]](**v)
				for k, v in obj_dict.items()}
		FileStorage.__objects = obj_dict

	def attributes(self):
		"""Returns the valid attributes and their types for classname"""
		attributes = {
			"BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
	return attributes
