import numpy as np
import pandas as pd


def read_csv():
    # Method to read the CSV file "Hospital_patients_datasets.csv" using pandas.
    # Returns: Pandas DataFrame containing the data from the CSV file.
    df = pd.read_csv("Hospital_patients_datasets.csv")
    return df


def check_duplicates():
    df = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    # Returns: The number of duplicated rows found in the DataFrame.
    duplicate_count = df.duplicated().sum()
    return duplicate_count


def check_null_values():
    df = read_csv()
    Null_count = df.isnull().sum()
    # Method to check for null (missing) values in the DataFrame.
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.
    return Null_count



def converting_dtype():
    df  = read_csv()
    # Method to convert 'ScheduledDay' and 'AppointmentDay' columns to datetime objects.
    # Returns: DataFrame with 'ScheduledDay' and 'AppointmentDay' columns converted to datetime objects.
    df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.tz_localize(None).dt.normalize()
    df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.tz_localize(None).dt.normalize()
    return df

def rename_columns():
    df = converting_dtype()
    # Method to rename some columns in the DataFrame.
    # Returns: DataFrame with certain column names changed to new names.
    column_mapping = {
        'Hipertension': 'Hypertension',
        'Handcap': 'Handicap',
        'SMS_received': 'SMSRecevied',
        'No-show': 'NoShow'
    }
    df.rename(columns=column_mapping, inplace=True)
    return df

def drop_columns():
    df = m1.rename_columns()
    # Method to drop unnecessary columns from the DataFrame.
    # Returns: DataFrame with specified columns dropped.
    columns_to_drop = ['PatientId', 'AppointmentID', 'Neighbourhood']
    df.drop(columns=columns_to_drop, inplace=True)
    return df


def create_bin():
    ds = drop_columns()
    #First Drop rows with Age == 0
    ds = ds[ds['Age'] != 0]
    # Generating labels for age intervals (e.g., '1 - 20', '21 - 40', etc.)
    labels = ["{0} - {1}".format(i, i + 20) for i in range(1, 118, 20)]
    # Using the pd.cut() function to categorize ages into groups(use bins = range(1, 130, 20) ,right=False and use the given labels)
    ds['Age_group'] = pd.cut(ds['Age'], bins = range(1, 130, 20), right = False, labels = labels)
    # Returning the modified dataset with assigned age groups
    return ds

def drop():
    df = create_bin()
    # Method to drop the original 'Age' column from the DataFrame.
    # Returns: DataFrame with the 'Age' column dropped.
    df.drop(columns=['Age'], inplace=True)
    return df


def convert():
    df = drop()
    # Method to convert 'NoShow' values into binary values (1 for 'Yes' and 0 for 'No').
    # Returns: DataFrame with 'NoShow' column values converted to 1s and 0s.
    df['NoShow'] = df['NoShow'].map({'Yes': 1, 'No': 0})
    return df


def export_the_dataset():
    df = convert()
    # write your code to export the cleaned dataset and set the index=false and return the same as 'df'
    df.to_csv('patients.csv', index=False)
    return df

# TASK 6: Load the Cleaned dataset 'patients.csv' to the database provided.
# follow the instruction in the Task 5 description and complete the task as per it.

# check if mysql table is created using "patients"
# Use this final dataset and upload it on the provided database for performing analysis in MySQL
# To run this task click on the terminal and click on the run project



