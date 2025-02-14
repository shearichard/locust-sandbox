![Locust logo](doco/images/locust_logo_0.png?raw=true "Locust Logo")

# Locust Sandbox
Some test scripts to show off the capabilities of the [locust](https://locust.io) load-testing framework.

# Running a load testing session
*It's necessary to invoke the virtualenv defined by Pipfile both for running the locust session and the script which provides the end points to test against. When running tmux I have found it impossible to start the pipenv managed virtualenv in two windows of the same console, to resolve this I have run the locust session in one window and the test endpoint script in another.* 

 1. Start the Flask app which provides the testing endpoints ```$python load_testbed.py```
 2. Start the locust session in a different console ```$locust```
 3. Use your web browser to visit the locust control panel at http://0.0.0.0:8089/ and use the onscreen controls to start the load testing session


# Tooling
## Virtualenv Management
[pipenv](https://pipenv.pypa.io/en/latest/) is in use as the virtualenv management tool.

## Linting
[flake8](https://flake8.pycqa.org/en/latest/) is used for code quality checking.

Be sure to check the .flake8 file for exclusions from the standard rules.

## Code Formatting
The [black](https://black.readthedocs.io/en/stable/) is installed for automatted code formatting, if that's your thing.
