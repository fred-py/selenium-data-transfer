"""---> Note: Initially unable to rename file to subs. The issue was that 
the methods from os or pathlib were looking at the working directory (automate_wordpress folder)
for the file to be renamed, however file had been saved under zip_file folder.
Now all files are under main main directory 'Automate_Wordpress'

--->> Run 'Path.cwd()' to check current working dir

Refer to pathlib link for more information"""

import zipfile # https://python.readthedocs.io/en/v2.7.2/library/zipfile.html + https://realpython.com/python-zipfile/
import time
from pathlib import Path #https://realpython.com/python-pathlib/#the-problem-with-representing-paths-as-strings
import os
import schedule
from schedule import repeat, every


# Zipfile directory
cwd_path = Path(f"/Users/frederico/automate_wordpress_package/automate_data_transfer/")


"""BUILD UNIT TEST FOR THIS FUNCTION"""
def extract_file():
    """Locate any .zip in cwd and extract csv to cwd"""

    # Use pathlib to locate files ending with specific extension
    zip_ex = list(Path(cwd_path).glob("*.zip"))
        
    if not zip_ex:
        return f"No .zip file found in {cwd_path} directory."
    # File is whatever zip file is currently in current working dir
    for file in zip_ex:
        # CSV to be saved to current working dir
        # Loading Zip file & creating zip object
        try:
            with zipfile.ZipFile(file, mode="r") as archive:
                for filename in archive.namelist(): # Listing all files in archive
                    # 1033 is the latest update of estimate form on the website
                    if "(1033)" in filename: # Check if 1033 is present in any file name in archive
                        archive.extract(filename, cwd_path)                    
                        print(f"{filename} has been extracted successfully")
                        time.sleep(5)
                        delete_zip()
                        time.sleep(5)
                        change_name()
        except FileNotFoundError:
            return f"Error: {file} not found in directory"




"""This function is called inside extract_file() function"""
def delete_zip():
    target_ex = ".zip" # Target file with extension .zip to be deleted
    file_list = os.listdir(cwd_path) # Get a list of all files in the directory
    # Filter and delete files with the target extension
    for file in file_list:
        if file.endswith(target_ex):
            file_path = os.path.join(cwd_path, file)
            try:
                os.remove(file_path)
                print(f"{file} has been deleted.")
            except PermissionError:
                print(f"Permission denied: Unable to delete {file}.")
            except Exception as e:
                print(f"Error deleting {file}: {e}")



"""This function is called inside extract file function"""
def change_name():
    """Locates files with .csv extension in main directory
    and changes file name to estimates.csv""" 
    #cwd_path = "/Users/frederico/automate_wordpress_package/automate_data_transfer" # Main directory
    target_ex = ".csv" # Target file with extension .csv to be renamed
    file_list = os.listdir(cwd_path) # Get a list of all files in the directory

    for file in file_list:
        # Iterate over files in directory to find target extension .csv
        if file.endswith(target_ex):
            """ Is file_path needed as it is greyed out?"""
            file_path = os.path.join(cwd_path, file)
            current_name = file
            new_name = "estimates.csv"
            os.rename(current_name, new_name)




"""FUNCTIONS CALLED AFTER """

#extract_file()




#schedule.every(1).minute.at(":20").do(extract_file)

#while True:
#    schedule.run_pending()
#    time.sleep(5)