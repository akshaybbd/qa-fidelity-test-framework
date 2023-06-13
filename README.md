# qa-fidelity-test-framework
**Below are the few links are commands for setup**
Download and Install Python 3 and above:-  Welcome to Python.org 
Download and Install Visual Studio Code:-  https://code.visualstudio.com/

Command to download all dependencies: pip install -r requirements.txt
Command to install webdriver manager : pip install webdriver-manager

Command to execute your feature file:  behave features\{path of feature file}

Command to execute your feature file with allure report: behave -f allure_behave.formatter:AllureFormatter -o reports/ features/\{path of feature file}

command to generate allure reports: allure serve reports
NOTE - you may need to set-up\install an allure seperately for that please refer this link https://www.programsbuzz.com/article/how-install-allure-windows

**Extensions you need to Add in your VS code**

vscode-icons
BDD highlighter
BDD Goto steps
Behave
BDD -Feature -Editor 
Cucumber
cucumber-gotostep
Pytest BDD
Cucumber Goto step


**Reference video: https://www.youtube.com/playlist?list=PLUDwpEzHYYLsARXz1o3Ldt1FnvRbvlxsS**


