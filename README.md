# swag-test-framework
This is an behave python selenium framework. Where QAE can automate API, web and mobile applications.

**Below are the few links are commands for setup**

Download and Install Python 3 and above:-  **https://www.python.org/**

Download and Install Visual Studio Code:-  **https://code.visualstudio.com/**

Command to download all dependencies: **pip install -r requirements.txt**

Command to install webdriver manager : **pip install webdriver-manager**

Command to execute your feature file:  **behave features\{path of feature file}**

Command to execute your feature file with allure report: **behave -f allure_behave.formatter:AllureFormatter -o reports/ .\features\{path of feature file}**

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


When it comes to writing automation code in Python, it's important to follow certain guidelines to ensure your code is maintainable, readable, and robust.
Here are some guidelines for writing automation code in Python:

**Use Descriptive Names**: Choose meaningful and descriptive names for variables, functions, and classes. This helps improve code readability and makes it easier for others to understand your code.

**Follow PEP 8 Style Guide**: PEP 8 is the official Python style guide that provides recommendations on how to format Python code. Adhering to PEP 8 guidelines makes your code consistent and easier to read. Some key points from PEP 8 include using 4 spaces for indentation, using lowercase with underscores for variable and function names, and limiting line length to 79 characters.

**Modularize Your Code**: Break your automation code into small, reusable functions or classes. This helps improve code maintainability and allows for easier testing and debugging. Each function or class should have a single responsibility and should be named accordingly.

**Handle Exceptions**: When writing automation code, it's crucial to handle exceptions properly. Wrap the sections of code that might raise exceptions in try-except blocks, and handle specific exceptions instead of catching all exceptions indiscriminately. This helps make your code more robust and prevents it from crashing unexpectedly.

**Add Comments**: Use comments to explain complex logic, document function or class behavior, and provide context where necessary. Comments help other developers (including yourself) understand the purpose and functionality of different parts of your code.

**Readability and Documentation**: Ensure your code is readable by using appropriate spacing, indentation, and line breaks. Additionally, consider adding inline documentation or docstrings to functions and classes to describe their inputs, outputs, and purpose. This makes it easier for others to understand and work with your code.

Every defination must be in lowercase.

All xpaths keys should be lowercase.

All file names should be in lowercase for folders config,features,steps,helper.

All utility names also in lowercase.

Every method/defination must have discription written in """ """

for eg:

def get_url(self):

"""Loads a web page in the current browser session."""

        """Loads a web page in the current browser session."""

your code

Whenever you raise a PR it must have discription.

Do not add too much empty spaces and empty new lines in code.

You can add multiple feature file for a maodule\squad\but try to keep only single step file single helper file.

Every step file must have either _steps.py or _impy.py as a postfix.

Every helper file must have _helper.py as a postfix.

Do not keep commented code in code repository.(If you needed it in future mention it in comment)

 main
+++
