### For code :

from myLib.logic import wiki

print(wiki())

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % .venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % make lint  
#check syntax # flake8 and pylint
pylint --disable=R,C _.py myLib/_.py
PYLINTHOME is now '/Users/vinee/Library/Caches/pylint' but obsolescent '/Users/vinee/.pylint.d' is found; you can safely remove the latter

---

Your code has been rated at 10.00/10

### Changing code to

main.py -->
from myLib.logic import wiki

res = wiki()
res = res

print(res)

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % make lint
#check syntax # flake8 and pylint
pylint --disable=R,C _.py myLib/_.py
**\*\***\***\*\*** Module main
main.py:4:0: W0127: Assigning the same variable 'res' to itself (self-assigning-variable)

---

Your code has been rated at 8.75/10 (previous run: 10.00/10, -1.25)

make: \*\*\* [lint] Error 4
