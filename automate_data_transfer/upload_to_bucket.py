#https://saturncloud.io/blog/how-to-write-csv-files-to-amazon-s3-using-python/
#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
import logging
import boto3
from botocore.exceptions import ClientError
import os
from aws_keys import access_keys, secret_keys
import zipfile


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options # Set up the drive to handle downloads.
from selenium.webdriver.support import expected_conditions as EC
from wordpress_keys import username, password
import time
# Imports for file_handling.py
import schedule
from file_handling import extract_file
from foward_estimates import submit_new_requests




options = Options() # Create a new options folder
options.add_argument("--headless") # Run headless

# Set the download directory and disable the download prompt
options.set_preference("browser.download.folderList", 2) #  Use custom download directory
options.set_preference("browser.download.manager.showWhenStarting", False)
#options.set_preference("browser.download.dir", "/Users/frederico/automate_wordpress_package/automate_data_transfer")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv") # Set the MIME types of files to automatically download (optional)



# Wordpress credentials
user = username
key = password  




def log_in():
    """Load url, locate user & password fields, enter credentials
    locate submit element and click to log in"""
    driver = webdriver.Firefox(options=options) # Create a WebDriver instance with FirefoxDriver and the custom options
    driver.get("https://unitedpropertyservices.au/wapd-admin/")

    l = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#user_login")))
    l.send_keys(user)

    p = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#user_pass")))
    p.send_keys(key)

    s = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#wp-submit")))
    s.click()
    # Calling other functions to locate and download file
    locate_submissions(driver)
    time.sleep(5)
    download(driver)
    time.sleep(5)
    driver.quit()




def locate_submissions(driver): # Called from log_in function
    """Locate and click 'Submissions' under 
    Elementor side menu tab locate and click download button"""
    # Locate Elementor element & click
    e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "toplevel_page_elementor")))
    e.click()

    # Locate & click Submissions 
    s = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Submissions")))
    s.click()




def download(driver): # Called from log_in function
    """Locate & click 'Download' element on 
    Submissions page"""   
    d = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
        "#elementor-form-submissions > div > div > div.tablenav.top > div.alignright > button")))
    d.click()



# Get the downloaded file's path within the dyno's filesystem
# This will depend on the browser and its capabilities
def locate_heroku_download(driver):
    downloaded_file_path = driver.capabilities['moz:profile'] + '/downloads/filename.csv'
    return downloaded_file_path


# Configure AWS Credentials
s3 = boto3.resource(
    's3',
    aws_access_key_id=access_keys,
    aws_secret_access_key=secret_keys 
)

# Print list of bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

s3_resource = boto3.resource('s3')
bucket_name = 'selenium-wordpress-united'

# File name
object_key = None
#csv_obj = s3_resource.get_object(Bucket=bucket_name, Key=object_key)
#body = csv_obj['Body']
#csv_string = body.read().decode('utf-8')

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
    
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True # Script does not return true

file = ("*.zip")

upload_file()