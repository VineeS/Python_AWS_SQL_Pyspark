1. First in the pytest the file name should start with test_filemame.py in which unit testing function will be written
2. To run any test import the python file that ypu are trying to test to test file ex : pytest1.py (need to test) test_pytest1.py (testing file)
3. Command --> pytest test_pystest1.py or pytest test_pytest1.py -v
4. The function name should always start with test* , if it does not start with test* it wont recognise the function
5. You can use decorator to run only limited test cases in above example --> you have 2 decorators @pytest.mark.number , @pytest.mark.strings
   and run pytest -v -m number to run only number or pytest -v -m strings to run only string tests. 6.
6. refer -- > https://www.youtube.com/watch?v=VKY-0LEmrwk&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=2
7. To skip the test use the @pytest.mark.skip(reason="YOUR REASON TO SKIP")
