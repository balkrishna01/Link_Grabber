
# Requirement of task

Task involves logging into Stack Overflow, performing a search query, and retrieving the URLs of the top 10 results. Subsequently, I need to export these URLs to an Excel file. 


# Steps for test execution:

1. Change `/Configurations/config.ini` as per requirements

2. Install python dependencies -
   > pip3 install -r requirements.txt

3. Execute `test_stackoverflow.py` to run the test
    > pytest -v -s testCases/test_stackoverflow.py

## Authors

- [@balkrishna01](https://www.github.com/balkrishna01)