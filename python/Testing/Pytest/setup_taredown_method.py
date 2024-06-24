# setup_teardown_method.py
import json

class Student:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student  # Return the entire student dictionary

    def close(self):
        # This method is currently a placeholder.
        pass
