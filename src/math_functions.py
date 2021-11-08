## add libraries

import os
import pandas as pd
import datetime
import time
import ast

## functions

def create_dataframe():

    '''this function takes all files in a data folder from the current directory and creates a dataframe from them'''

    files = os.listdir('Data')

    df = pd.DataFrame()

    path = os.getcwd() + "\\Data" + "\\"

    for i in files:
        data = pd.read_csv(path + i)
        df = df.append(data)
    
    return df
#
#
#
def drop_and_compare_duplicates(df):

    '''this function drops all duplicated rows and compared before and after'''

    before_dropping_duplicates = df.shape

    df = df.drop_duplicates()

    after_dropping_duplicates = df.shape

    return print(before_dropping_duplicates[0] - after_dropping_duplicates[0], 'rows have been dropped!')
#
#
#
# def drop_and_compare_duplicates_id(df): TODO
#
#
#
def get_data_from_timestamp(column, df):
    
    '''this function takes a timestamp and creates 3 new columns for date,time,weekday out of it'''  
    
    date = []
    time = []
    weekday = []
    
    for i in df[f'{column}']:
        date.append(datetime.datetime.fromtimestamp(int(i)).strftime('%Y-%m-%d'))
        time.append(datetime.datetime.fromtimestamp(int(i)).strftime('%H:%M:%S'))
        weekday.append(datetime.datetime.fromtimestamp(int(i)).strftime('%A'))
    
    df[f'{column}' + '_date'] = date
    df[f'{column}' + '_time'] = time
    df[f'{column}' + '_weekday'] = weekday
    
    return df
#
#
#
def get_category_data(column, df):

    '''this function takes a timestamp and creates 3 new columns for date,time,weekday out of it'''  

    name = []
    analytics_name = []
    slug = []
    parent_name = []

    for i in df[f'{column}']:

        dictionary = ast.literal_eval(i)
        
        name.append(dictionary.get('name'))
        analytics_name.append(dictionary.get('analytics_name'))
        slug.append(dictionary.get('slug'))
        parent_name.append(dictionary.get('parent_name'))

    df[f'{column}' + '_name'] = name
    df[f'{column}' + '_analytics_name'] = analytics_name
    df[f'{column}' + '_slug'] = slug
    df[f'{column}' + '_parent_name'] = parent_name

    return df
#
#
#