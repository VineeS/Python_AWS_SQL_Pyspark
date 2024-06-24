import pytest1
import pytest

@pytest.mark.number
def test_add():
    assert pytest1.add(7,3) == 10

## this will skip the test
@pytest.mark.skip(reason = "Do not run")
def test_add_2():
    assert pytest1.add(7,4) == 10

@pytest.mark.strings
def test_string():
    result = pytest1.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "orld" in result

@pytest.mark.strings
def test_string_2():
    assert pytest1.product("Hello ", 3) == "Hello Hello Hello "