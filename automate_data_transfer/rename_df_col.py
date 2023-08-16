
import pandas as pd

def rename_col(data):
    data.rename(columns={
        "Submission ID": "Submission", 
        "Select Service(s)": "Services", 
        "Created At": "Date"}, inplace=True)
    return data