# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:01:09 2020

@author: lenovo
"""


from sys import exit
from argparse import ArgumentParser
from configs import configurations
from utils.filehandler import FilePreprocess
from CRD.functions import DataStoreCRD


# Adding/Enabling CommandLineArguments: --datastore
parser = ArgumentParser()
parser.add_argument('--datastore', help='Enter the datastore absolute path.')
args = parser.parse_args()

# Selecting the DataStore Directory.
# Select user provided datastore path else, select the default path.
if args.datastore:
    db_path = args.datastore
else:
    db_path = configurations.DEFAULT_DB_PATH

# Create a datastore directory.
directory_created = FilePreprocess(db_path).create_folder()
if not directory_created:
    print(f"Permission denied: You can not create the directory `{db_path}`.\n")
    exit(0)


json_data = {
    "vedha": {
        "vedha": "1",
        "roll_no": "26",
        "Time-To-Live": 5000,
    },
    "sathya": {
        "sathya": "2",
        "roll_no": "32",
        "Time-To-Live": 50,
    },
    "raja": {
        "raja": "3",
        "roll_no": "33",
    },
    "raj": {
        "raj": "4",
        "roll_no": "45",
        "Time-To-Live": 250,
    }
}


################################
''' CREATE DATA IN DATASTORE '''
_valid_data, message = DataStoreCRD().check_create_data(json_data, db_path)
print(message)
################################