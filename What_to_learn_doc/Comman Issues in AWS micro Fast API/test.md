### now we are doing testing hence

1. writing the test case in test_logic.py
   code -

from myLib.logic import wiki

def test_wiki():
assert 'god' in wiki()

2. Go to Makefile add - python -m pytest -vv --cov=myLib test_logic.py
   the --cov will show how much test ccoverage is done for the particular directory
3. run - make test
   output -

make test
#test
python -m pytest -vv --cov=myLib test_logic.py
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.12.3, pytest-7.1.0, pluggy-1.5.0 -- /Users/vinee/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/vinee/Desktop/PythonInterview/Python-interview-2024/Python-AWS-FastAPI-microservicces
plugins: cov-3.0.0
collected 1 item

test_logic.py::test_wiki PASSED [100%]

=========================================================================== warnings summary ===========================================================================
../../../../.venv/lib/python3.12/site-packages/\_pytest/assertion/rewrite.py:692
../../../../.venv/lib/python3.12/site-packages/\_pytest/assertion/rewrite.py:692
/Users/vinee/.venv/lib/python3.12/site-packages/\_pytest/assertion/rewrite.py:692: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
and isinstance(item.value, ast.Str)

../../../../.venv/lib/python3.12/site-packages/\_pytest/assertion/rewrite.py:694
/Users/vinee/.venv/lib/python3.12/site-packages/\_pytest/assertion/rewrite.py:694: DeprecationWarning: Attribute s is deprecated and will be removed in Python 3.14; use value instead
doc = item.value.s

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

---------- coverage: platform darwin, python 3.12.3-final-0 ----------
Name Stmts Miss Cover

---

myLib/**init**.py 0 0 100%
myLib/logic.py 4 0 100%

---

TOTAL 4 0 100%

==================================================================== 1 passed, 3 warnings in 2.11s =====================================================================
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces %

### The above code shows 100% code covergae
