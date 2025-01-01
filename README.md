# python-pytest-request
This repo has Backend/API automation framework using python,pytest &amp; request

# Step to use API Automation
- Download Python & Install
- Download Pycharm & Install
- Install Pytest framework for execution
- Install request using below command - https://pypi.org/project/requests/
pip install requests
- By default, request library will be available in python
- Free website to learn API Automation
https://reqres.in/

# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate
# Install dependencies
pip install -r requirements.txt
# deactivate
deactivate

# Run Using pytest in multiple environment
pytest -s -m "jsonTest" --host=prod --disable-pytest-warnings

# Run All Tests
pytest -s --host=prod --disable-pytest-warnings

# with html report
pytest -s --host=prod --disable-pytest-warnings --html=report.html

# Run With markers
pytest -s -m "jsonCompareTest" --host=prod --disable-pytest-warnings --html=report.html