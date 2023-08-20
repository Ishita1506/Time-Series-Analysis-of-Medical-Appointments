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


