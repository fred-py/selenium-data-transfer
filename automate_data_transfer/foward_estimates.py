"""Selenium Indexed Documentation""" 
#https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # https://selenium-python.readthedocs.io/waits.html
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options # Set up the drive to handle downloads.
from selenium.common.exceptions import TimeoutException # Run Headless Browser
from selenium.webdriver.support import expected_conditions as EC # https://selenium-python.readthedocs.io/waits.html
from pathlib import Path
import pandas as pd
import time
import schedule
from schedule import repeat, every
from rename_df_col import rename_col

options = Options() # Create a new options folder
options.add_argument("--headless") # Run headless



"""This function os used for testing only instead of sending actual names"""
def input_id(sub_id,driver):
	d = WebDriverWait(driver, 6).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "#inputContactName"))
		)
	return d.send_keys(f"{sub_id}")


def input_name(name, driver):
	# Waits until first element is located
	d = WebDriverWait(driver, 6).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "#inputContactName"))
	)
	return d.send_keys(f"{name}")


def input_email(email, driver):
	d = driver.find_element(By.CSS_SELECTOR, "#inputEmail")
	return d.send_keys(f"{email}")


def input_mobile(mobile, driver):
	d = driver.find_element(By.CSS_SELECTOR, "#inputPhoneNumber")
	return d.send_keys(f"{mobile}")
	

def input_address(address, suburb, postcode, driver): # Takes values from 3 columns to form full address
	d = driver.find_element(By.CSS_SELECTOR, "#inputAddress")
	return d.send_keys(f"{address} {suburb} {postcode}")


def input_message(msg, serv, driver): #also includes services 
	d = driver.find_element(By.CSS_SELECTOR, "#inputJobDescription")
	return d.send_keys(f"Message: {msg} \nService(s) selected: {serv}")


def click_submit(driver):
	"""Locate and click the 'submit' button 
	Then wait for element to load on new url[Thank you for your enquiry/page]"""
	d = driver.find_element(By.CSS_SELECTOR, "#buttonSubmit")
	d.click()
	# Wait for element to appear on new page after submission is completed
	d = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "#StatusMessage"))
		)




def submit_new_requests():
	"""Finding unique values in df ->> 'New Estimate Request(s)'
	Check df (estimates file) against df2 (submitted file)
	Unique values will be passed on to service mate"""
	"""IF NO UNIQUE VALUES PRINT NO NEW ESTIMATES"""
	# Iterate over unique_to_df with .intertuples()
	# https://sparkbyexamples.com/pandas/pandas-get-list-of-all-duplicate-rows/
	driver = webdriver.Firefox(options=options) # Create a WebDriver instance with FirefoxDriver and the custom options
	
	# Must reset index, inplace=True to change the original file
	# df contains potential new estimate requests, if true unique values(new requests) will be processed 
	df = pd.read_csv("/Users/frederico/automate_wordpress_package/automate_data_transfer/estimates.csv", index_col=0).reset_index()
	rename_col(df)
	# df2 contains all estimate requests submitted to date, this is used to compare against df and find unique values/new requests
	df2 = pd.read_csv("/Users/frederico/automate_wordpress_package/automate_data_transfer/submitted_dir/submitted.csv", index_col=0).reset_index()
	rename_col(df)

	# On the newly generated _merged col, "left_only" value indicates value only present on the left df(newly downloaded csv)
	new = "left_only" # 'new estimate requests'
	merged_df = df.merge(df2, how="outer", indicator=True)
	new_est = merged_df[merged_df["_merge"] == new] 

	for col in new_est.itertuples():
		driver.get("https://book.servicem8.com/request_booking?uuid=c157a4d5-f730-4b77-90b7-1d8f405736db")
		
		sub_id = col.Submission # For testing
		name = col.Name
		email = col.Email
		mobile = col.Mobile
		address = col.Address
		suburb = col.Suburb
		postcode = col.Postcode
		msg = col.Message
		serv = col.Services

		#input_id(sub_id)
		input_name(name,driver)
		input_email(email, driver)
		input_mobile(mobile, driver)
		input_address(address, suburb, postcode, driver)
		input_message(msg, serv, driver)
		click_submit(driver)
	
	time.sleep(5)
	rename_estimate()
	


"""NOW YOU MUST WRITE CODE THAT CONCATNATE new_SUBMITED.CSV 
with existing submitted.csv in submitted_dir"""

def rename_estimate():
	"""Rename estimates.csv once new estimates have been submitted
	and save submitted.csv into submitted_dir replacing the existing submitted file"""
	original = "/Users/frederico/automate_wordpress_package/automate_data_transfer/estimates.csv" # Define path to original file
	updated = "submitted.csv" # Define new name for the file
	new_folder = "/Users/frederico/automate_wordpress_package/automate_data_transfer/submitted_dir/" # Define full path of new folder
	# Combine the new folder path with the new file name to get the new full path
	new_path = Path(new_folder) / updated
	# Rename the file and move it to the new location
	Path(original).rename(new_path)
	return f"Latest new_submitted.csv file saved in directory"







#submit_new_requests()
#rename_estimate()

#schedule.every(1).minute.at(":25").do(submit_new_requests)

#while True:
#    schedule.run_pending()
#    time.sleep(5)