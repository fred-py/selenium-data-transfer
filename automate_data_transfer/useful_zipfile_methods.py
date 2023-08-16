# https://realpython.com/python-zipfile/#what-is-a-zip-file

import zipfile
import datetime
import pandas as pd


"""with zipfile.ZipFile("elementor-submissions-export-2023-08-01.zip") as archive:
    archive.printdir()"""


# Target valid zipfile only by wrapping it in try...except statement
try:
    with zipfile.ZipFile("elementor-submissions-export-2023-08-01.zip") as archive:
        archive.printdir()
except zipfile.BadZipFile as error:
    print(error)



# Perform quick check on ZIP file and list the names of its member files
with zipfile.ZipFile("elementor-submissions-export-2023-08-01.zip", mode="r") as archive:
    for filename in archive.namelist():
        print(filename)

with zipfile.ZipFile("elementor-submissions-export-2023-08-01.zip", mode="r") as archive:
    for info in archive.infolist():
        print(f"Filename: {info.filename}")
        print(f"Modified: {datetime.datetime(*info.date_time)}")
        print(f"Normal size: {info.file_size} bytes")
        print(f"Compressed size: {info.compress_size} bytes")
        print("-" * 20)


# Reading a file
with zipfile.ZipFile("elementor-submissions-export-2023-08-01.zip", mode="r") as archive:
    for line in archive.read("elementor-submissions-export-form_v2 (1033)-2023-07-28.csv").split(b"\n"):
        print(line)


#enquiries = pd.read_csv("elementor-submissions-export-form_v2 (1033)-2023-07-28.csv")
#enquiries