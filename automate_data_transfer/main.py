#!/Users/frederico/automate_wordpress_package/venv/bin/python


"""Selenium Indexed Documentation""" 
#https://selenium-python.readthedocs.io/

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
options.set_preference("browser.download.dir", "/Users/frederico/automate_wordpress_package/automate_data_transfer")
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


schedule.every(2).hours.at(":02").do(log_in)
schedule.every(2).hours.at(":04").do(extract_file)
schedule.every(2).hours.at(":06").do(submit_new_requests)


while True:
    schedule.run_pending()
    time.sleep(5)

#log_in()
#extract_file()
#time.sleep(5)
#submit_new_requests()




""" Testing if login was successful
Enter the wrong credentials on the login 
page to inspect HTML for the error message"""
# Wait for the page to load after login
##WebDriverWait(driver=driver, timeout=10).until(
##    lambda x: x.execute_script("return document.readyState === 'complete'")
##)
##error_message = "The password you entered for the username"
# Get error if any
##errors = driver.find_elements("css selector", "login_error")
# print the errors optionally
##for e in errors:
##    print(e.text)
# if we find that error message within errors, then login is failed
##if any(error_message in e.text for e in errors):
##    print("[!] Login failed")
##else:
##    print("[+] Login successful")