#!/usr/bin/python3
"""
This is "base" module
"""


import json
from turtle import *
import csv
from os import path


class Base:
    """A class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization for the object"""

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        unique_dicts = {}
        for dictionary in list_dictionaries:
            unique_dicts[dictionary['id']] = dictionary

        unique_list = list(unique_dicts.values())
        return json.dumps(unique_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        if list_objs is None:
            list_objs = []

        with open("{}.json".format(cls.__name__), "w", encoding="UTF-8") as ff:
            data = cls.to_json_string([x.to_dictionary() for x in list_objs])
            ff.write(data)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        if not path.exists("{}.json".format(cls.__name__)):
            return []

        with open("{}.json".format(cls.__name__), "r", encoding="UTF-8") as ff:
            data = ff.read()
            my_list = cls.from_json_string(data)
            instance_list = []
            for ins in my_list:
                instance_list += [cls.create(**ins)]

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""

        name = cls.__name__
        with open(f"{name}.csv", "w", newline="", encoding="UTF-8") as ff:
            if list_objs is None or len(list_objs) == 0:
                ff.write("[]")
            else:
                if name == "Square":
                    fields = ["id", "size", "x", "y"]
                elif name == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]

                writer = csv.DictWriter(ff, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""

        name = cls.__name__
        if path.exists(f"{name}.csv"):
            with open(f"{name}.csv", "r", encoding="UTF-8") as ff:
                my_list = []

                if name == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif name == "Square":
                    fields = ["id", "size", "x", "y"]

                csv_ff = csv.DictReader(ff, fields)
                for row in csv_ff:
                    my_d = {}
                    for k, v in row.items():
                        my_d[k] = v
                    my_list.append(my_d)

                ins_list = []
                for o in my_list:
                    di = {}
                    for k, v in zip(fields, o.values()):
                        di[k] = int(v)
                    ins_list.append(cls.create(**di))
            return ins_list
        else:
            return []

    def draw(list_rectangles, list_squares):
        """that opens a window and draws all the Rectangles and Squares"""

        for rectangle in list_rectangles:
            x = Turtle()
            x.color("red", "yellow")
            x.begin_fill()
            x.fd(ractangle.width * 10)
            x.lt(90)
            x.fd(ractangle.height * 10)
            x.lt(90)
            x.fd(ractangle.width * 10)
            x.lt(90)
            x.fd(ractangle.height * 10)
            x.end_fill()
            done()
