Explanation
---
Current tests were created using Python, Selenium and PyTest.
 - Tests are optimised for Chrome browser, it works 100% good
 - Tests were **not optimised** for Firefox browser due to difficulties with handling shadow root by mozilla browser api.

Preconditions
---
Make sure you have `git`, `python3` and `pip3` installed. If not, please do so by googling and following the instructions on the official resources.

Recommended `python` version is 3.10

Prepare environment
---
Clone the project to your local machine and navigate to the project directory:
```shell
git clone git@github.com:IgorDodukh/mb-test.git
cd mb-test
```
Install and setup virtualenv for the project:
```shell
pip3 install virtualenv
virtualenv --python python3 venv
source venv/bin/activate
```
* Install all packages required for the tests run:
```shell
pip3 install -r requirements.txt
```
----
Same actions you can de within PyCharm IDE via UI with hints

Run tests
---
Once the environment is ready the tests can be executed. Run the following command to do so:
```shell
pytest tests
```

Test results
---
According to the test task, test outputs can be found in `mb-test/artefacts` after the test run.
