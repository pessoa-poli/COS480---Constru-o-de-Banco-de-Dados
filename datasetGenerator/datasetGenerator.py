# This program should create a big enough dataset  for us to work with.
import names
import random
import time
import sys
from random_date_generator import *
from cpf_generator import cpf
from io import StringIO
import os

##############################
####### SETTINGS
##############################
DATASET_SIZE_IN_MB = 4*1014 #Change this var to fit your needs

DATASET_OUTPUT_DIRECTORY = "./dataset.csv"

# Define the start and the end period to choose a random date from.
RANDOM_DATE_START = "01/01/1990"
RANDOM_DATE_END = "01/01/2022"

# Defines the salary range for random salary generation
MAX_SALARY = 50000
MIN_SALARY = 950

# Defines the max size in MB of the string being generated before printing it to file
MAX_MB_PER_BATCH = 50


############################################


def GenerateName():
    """
    Generates a name using the names lib: https://pypi.org/project/names/
    Effectively Returns a full name in string form.
    """
    return names.get_full_name()

def GenerateRandomDate():
    """Generate a random date between RANDOM_DATE_START AND RANDOM_DATE_END to be used as birthday."""
    return random_date(RANDOM_DATE_START, RANDOM_DATE_END, random.random())


def GenerateCPF():
    return cpf()

def GenerateSalary():
    return round(MIN_SALARY + random.random() * (MAX_SALARY - MIN_SALARY), 2)

def GenerateRecord():
    return f"{GenerateName()},{GenerateRandomDate()},{GenerateCPF()},{GenerateSalary()}"

def GenerateString(max_bytes):
    return 

def GenerateDatasetPortion():
    """Generates around MAX_MBYTES_PER_BATCH data"""
    string_io = StringIO()
    while (sys.getsizeof(string_io.getvalue())/(1024*2) < MAX_MB_PER_BATCH):
        #print(f"We are at size {sys.getsizeof(string_io.getvalue())/(1024*2)}MB of {DATASET_SIZE_IN_MB}MB")
        string_io.write(GenerateRecord() + "\n")
    return string_io.getvalue()

def getDatasetSizeInMB():
    return os.path.getsize(DATASET_OUTPUT_DIRECTORY)/(1024*2)     

def GenerateDataset():
    with open(DATASET_OUTPUT_DIRECTORY, "a") as dataset_file:
        start_size_in_MB = getDatasetSizeInMB()
        print(f"Initial dataset size is {start_size_in_MB}MB")
        
        while getDatasetSizeInMB() < DATASET_SIZE_IN_MB:
            print(f"We are at size {getDatasetSizeInMB()}MB of {DATASET_SIZE_IN_MB}MB")
            portion = GenerateDatasetPortion()
            dataset_file.write(portion)
    print(f"Final dataset size was {getDatasetSizeInMB()}MB")

GenerateDataset()