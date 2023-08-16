
Login automation & instructions
https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python

->>> Set up Selenium
Check book "Automating the boring stuff with Python"
Page 740~ 
Firefox works best, no need for driver 

Webdriver Elements Finder Documentation
# https://www.selenium.dev/documentation/webdriver/elements/finders/

Selenium Index - Complete Walkthrough With Examples
https://selenium-python.readthedocs.io/

Modules/packadges
1. pip install selenium
2. pip install chromedriver-py (other options available)
# https://github.com/SergeyPirogov/webdriver_manager
3.pip install webdriver-manager
    refer to link above. Driver manager makes it easier to work work with selenium


# TO DOWNLOAD FILES
# https://www.browserstack.com/guide/download-file-using-selenium-python

# TO ALLOW SCRIPT TO RUN ON THE BACKGROUND
# Ask chatgpt for more information if needed
On terminal: 
>>> export VISUAL=nano
>>> crontab -e
Wake up every 2h 
>>> 0 */2 6-12 * * pmset repeat wakeorpoweron MTWRF 06:00:00 


# DEPLOYMENT
__Docker, CI(Continuous Integration) *GREAT READ AND instructions
https://realpython.com/python-continuous-integration/#what-is-continuous-integration

