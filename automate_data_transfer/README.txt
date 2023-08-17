
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


# DEPLOYMENT (LINK FOR REFERENCE ONLY - WILL DEPLOY DIRECTLY ON HEROKU DYNO)
__Docker, CI(Continuous Integration) *GREAT READ AND instructions
https://realpython.com/python-continuous-integration/#what-is-continuous-integration



#---- HEROKU SET UP AND DEPLOYMENT

https://devcenter.heroku.com/articles/procfile
https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-python
https://devcenter.heroku.com/articles/python-rq


Prerequisites:

Make sure you have a Heroku account. If not, sign up for one.
Install the Heroku CLI on your local machine: https://devcenter.heroku.com/articles/heroku-cli
Prepare Your Script:

Make sure your Selenium Python script is ready and tested locally.
Ensure that your script uses appropriate error handling and logging mechanisms.
Create a Heroku App:

Open your terminal or command prompt.
Navigate to your project directory using cd /path/to/your/project.
Run the following commands:

>>>heroku login  # Log in to your Heroku account
>>>heroku create your-app-name  # Replace 'your-app-name' with your desired app name

Configure Buildpacks:

Ensure a requirements.txt file is present on ROOT directory and this should avoid error 
"""! [remote rejected] master -> master (pre-receive hook declined)"""
This error happened when first running 'git push heroku master' as heroku could not
identify buildpack. 

# ---- Data Storage with AWS S3 Buckets
Data will saved, read and modified from an S3 Buckets
Once bucket is created, create access point -> choose VPC for lower costs.