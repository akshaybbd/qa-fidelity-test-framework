# swag-test-framework
This is an behave python selenium framework. Where QAE can automate API, web and mobile applications.

**Below are the few links are commands for setup**

Download and Install Python 3 and above:-  **https://www.python.org/**

Download and Install Visual Studio Code:-  **https://code.visualstudio.com/**

Command to download all dependencies: **pip install -r requirements.txt**

Command to install webdriver manager : **pip install webdriver-manager**

Command to execute your feature file:  **behave features\{path of feature file}**

Command to execute your feature file with allure report: **behave -f allure_behave.formatter:AllureFormatter -o reports/ features/\{path of feature file}**

command to generate allure reports: allure serve reports

NOTE - you may need to set-up\install an allure seperately for that please refer this link **https://www.programsbuzz.com/article/how-install-allure-windows**

**Extensions you need to Add in your VS code**

vscode-icons,
BDD -Feature-Editor,
BDD Goto steps,
BDD Highlighter,
Behave,
Cucumber,
Cucumber (Gherkin) Full Support,
Cucumber Goto step,
Feature Syntax Highlight and Snippets (Cucumber/Gherkin),
Pytest BDD,
vscode-cucumberjs-navigator.

**Reference video: https://www.youtube.com/playlist?list=PLUDwpEzHYYLsARXz1o3Ldt1FnvRbvlxsS**



**Code guidelines**
Every defination must be in lowercase.
All xpaths keys should be lowercase.
All file names should be in lowercase for folders config,features,steps,helper.
All utility names also in lowercase.
Every method/defination must have discription written in """ """
for eg:
def get_url(self):
        """Loads a web page in the current browser session."""
        your code

Whenever you raise a PR it must have discription.
Do not add too much empty spaces and empty new lines in code.
You can add multiple feature file for a maodule\squad\but try to keep only single step file single helper file.
Every step file must have either _steps.py or _impy.py as a postfix.
Every helper file must have _helper.py as a postfix.
+++
