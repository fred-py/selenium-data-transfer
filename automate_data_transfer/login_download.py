

"""Selenium Indexed Documentation""" 
#https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options # Set up the drive to handle downloads.
from selenium.common.exceptions import TimeoutException # Run Headless Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wordpress_keys import username, password
import time
import schedule
from schedule import repeat, every



options = Options() # Create a new options folder
options.add_argument("--headless") # Run headless

# Set the download directory and disable the download prompt
options.set_preference("browser.download.folderList", 2) #  Use custom download directory
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", "/Users/frederico/automate_wordpress")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv") # Set the MIME types of files to automatically download (optional)

# Wordpress credentials
user = username
key = password



def log_in():
    """Load url, locate user & password fields, enter credentials
    locate submit element and click to log in"""
    driver = webdriver.Firefox(options=options) #WebDriver instance with FirefoxDriver and the custom options
    driver.get("https://unitedpropertyservices.au/wapd-admin/")
    driver.find_element("id", "user_login").send_keys(user)
    driver.find_element("id", "user_pass").send_keys(key)  # Find input field for password and add below
    driver.find_element("name", "wp-submit").click()
    locate_submissions(driver)
    time.sleep(5)
    download(driver)
    time.sleep(5)
    driver.quit()


"""Testing if login was successful
1. Enter the wrong credentials on the login page to inspect 
HTML for the error message"""
# Wait for the page to load after login
##driver2 = webdriver.Firefox(options=options) # Opens browser named 2 as this is outside function
##WebDriverWait(driver=driver2, timeout=10).until(
##   lambda x: x.execute_script("return document.readyState === 'complete'")
##)
##error_message = "The password you entered for the username"
# Get error if any
##errors = driver2.find_elements("css selector", "login_error")
# print the errors optionally
##for e in errors:
##    print(e.text)
# if we find that error message within errors, then login is failed
##if any(error_message in e.text for e in errors):
##    print("[!] Login failed")
##else:
##    print("[+] Login successful")


"""Stage 3 - accessing 'Submissions' under 'Elementor' side menu tab"""

# Once logged in find elementor button on left side menu & click
# located at <div id=admmenuback 

def locate_submissions(driver): # Called from long_in function
    """Locate and click 'Submissions' under Elementor side menu tab
    locate and click download button"""
    # Locate Elementor element & click
    e = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "toplevel_page_elementor"))
                )
    e.click()

    # Locate & click Submissions 
    s = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Submissions")) 
    )
    s.click()

   
# Locate & click 'download' button
def download(driver): # Called from long_in function
    """WebDriver Wait does not work for some reason"""   
    driver.find_element(By.CSS_SELECTOR, "#elementor-form-submissions > div > div > div.tablenav.top > div.alignright > button").click()

log_in()

#schedule.every(1).hour.at(":15").do(log_in)

#while True:
#    schedule.run_pending()
#    time.sleep(5)