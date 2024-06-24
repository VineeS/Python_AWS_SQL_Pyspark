# test_sample.py
import json
import pytest

@pytest.fixture
def sample_fixture():
    return {"key": "value"}

@pytest.mark.parametrize("_", range(3))  # Run the test 3 times
def test_using_fixture(sample_fixture, _):
    assert sample_fixture["key"] == "value"

def add(a,b):
    return a+b

@pytest.mark.parametrize('num1,num2, result',[(7,3,10),(2,5,7),(3,2,5)] )
def test_add(num1,num2,result):
    assert add(num1,num2) == result


class Student:
    def __init__(self):
        self.__data = None

    def connect(self,data_file):
            with open(data_file) as json_file:
                self.__data = json.load(json_file)

    def get_data(self,name):
        for student in self.__data['students']:
            if student['name'] == name:
                 return student
            
            
@pytest.fixture
def student_db():
    db = Student()
    db.connect('data.json')
    return db
            
@pytest.mark.parametrize("name, expected_id, expected_name", [
    ("Vinee", 1, "Vinee"),
])
def test_student(student_db, name, expected_id, expected_name):
    student_data = student_db.get_data(name)
    assert student_data is not None, f"Student '{name}' not found"
    assert student_data['id'] == expected_id
    assert student_data['name'] == expected_name