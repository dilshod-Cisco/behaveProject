Python Behave with Selenium
---------------------------
1) >>> Project Creation 
2) >>> First Selenium Test

- Install selenium package
- install behave package
- https://www.selenium.dev/downloads/
- Or open which browser you use and download 'webdriver' directly
  - 1) create this file - "orangehrm.feature" then run command below in Terminal
- Execute this command should take place on Terminal: -> "behave features\orangehrm.feature"
  - 2) create this file "orangehrmlogin.feature" run command below in the Terminal
- Executing command on the Terminal: -> behave features\orangehrmlogin.feature
- 3) create this file "scenariobg.feature" and then run command below in the Terminal
    - Execute this command on Terminal: -> behave features\scenariobg.feature
  

# Pre-requisite:
----------------
1. install:-> allure-behave 
2. pip install allure-behave
  >>> in order to install allure-behave go to the File
    new project settings + settings for new project
    python interpreter + allure-behave +install
  > --------------------------------------------
  > This command will create new folder 
  > where reports will be generated in the terminal Execute this command down below:
  > "behave -f allure_behave.formatter:AllureFormatter -o reports/ features"
> ----------------------------------------------------------------------------
  > you can specify which folder you want to Execute in this case I choose Directory "features"
  > if you want to specify Execution after directory features/and then folderName  
 this command will create HTML FORMAT from json file
  > allure serve reports/
