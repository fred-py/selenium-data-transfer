
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


-->>> TESTING SELENIUM WITH PYTEST
https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/waits/test_waits.py


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


***CLOUD SET UP AND DEPLOYMENT***
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
#-->> Install firefox and geckodriver 
>>>heroku buildpacks:add https://github.com/pyronlaboratory/heroku-integrated-firefox-geckodriver

Update Heroku's environment variables to store the following path strings.
s.heroku.com/buildpacks/pyronlaboratory/hero
FIREFOX_BIN: /app/vendor/firefox/firefox

Alternatively, you can even use /app/vendor/firefox/firefox-bin

GECKODRIVER_PATH: /app/vendor/geckodriver/geckodriver

LD_LIBRARY_PATH: /usr/local/lib:/usr/lib:/lib:/app/vendor

PATH: /usr/local/bin:/usr/bin:/bin:/app/vendor/

These configuration variables can be updated via Heroku CLI as follows:

Executable command: 
>>>heroku config:set <ENV_VARIABLE>=<ABSOLUTE_PATH>



Configure Buildpacks: 
Ensure a requirements.txt file is present on ROOT directory and this should avoid error 
"""! [remote rejected] master -> master (pre-receive hook declined)"""
This error happened when first running 'git push heroku master' as heroku could not
identify buildpack. 

https://devcenter.heroku.com/articles/heroku-cli-commands

#** Configure Heroku to run worker dyno instead of default web dyno

On Procfile add: worker: python path_to_main_file/main.py
Deploy again Git push heroku...
*NOTE: Since main is not on root directory the file path must be added on Procfile
In this case root is automate_wordpress_package and main.py is in automate_data_transfer
so ---> worker: python automate_data_transfer/main.py 
>>>heroku ps:scale worker=1

# Set up stack or migrate to a New Stack
https://devcenter.heroku.com/articles/stack
Firefox and geckodriver are only compatible with heroku-20< New Stack. 
To set/migrate:
>>>heroku stack:set heroku-22

# Set up enviroment variables on Heroku
On terminal
>>>heroku config:set USER=username
>>>heroku config:set KEY=password

To access key variables on script:
>>>user = os.environ["USER"]
>>>key = os.environ["KEY"]


# Set up Background Tasks in Python with RQ (Redis Queue)
*** This may be needed (NOT SURE AT THIS STAGE) in order to run *worker dyno in Procfile to run main script
Follow instructions on link below:
https://devcenter.heroku.com/articles/python-rq





# ---- Data Storage with AWS S3 Buckets
Data will saved, read and modified from an S3 Buckets
Once bucket is created, create access point -> choose VPC for lower costs.


# --->>> AWS LAMBDA FUNCTIONS
This may be used instead of Heroku.

1. Create custom lambda function eg. download_csv
2. Select trigger event: EventBridge(CloudWatch Events)
3. Select create new rule
4. Rule type: Schedule expression
    rate expression is easy to set up eg: rate(2 hours) runs every 2 hours
    for more control and customisation use cron 
5. Click add