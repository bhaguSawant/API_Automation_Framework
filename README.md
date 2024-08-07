# Python API Automation Framework

# Tech Stack
-Python 3.12
-Request -HTTP Request
-Pytest-Testing Framework
-Reporting -Allure Report,Pytest HTML
-Test Data -CSV,Excel,Json,Faker
-Advance API Testcase -Jsonschema
-Parallel Execution -x distribute(xdist)

#How To Install Packages

```pip install request pytest pytest-html faker allure-pytest jsonschema```

#How To run your testcase parallel

```pip install pytest-xdist```

### How to add .gitignore file?

copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm+all

###How to run basic things in allure report
```pytest tests/crud/test_create_booking.py --alluredir=allure_result -s ```