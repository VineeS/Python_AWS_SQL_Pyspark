import pytest # type: ignore
from setup_taredown_method import Student

db = None
def setup_module():
    print("..setup_modeule..")
    global db
    db = Student()
    db .connect('data.json')

def teardown_module():
    print("..teardown_module..")
    db.close()

def test_student():
    vinee_data = db.get_data('Vinee')
    print("In test_student")
    assert vinee_data is not None, "Student 'Vinee' not found"
    assert vinee_data['id'] == 1
    assert vinee_data['name'] == "Vinee"