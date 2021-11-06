
def create_dataframe():

    import os
    import pandas as pd

    '''this function takes all files in a data folder from the current directory and creates a dataframe from them'''

    files = os.listdir('Data')

    df = pd.DataFrame()

    path = os.getcwd() + "\\Data" + "\\"

    for i in files:
        data = pd.read_csv(path + i)
        df = df.append(data)
    
    return df



def drop_and_compare_duplicates():

    '''this function drops all duplicated rows and compared before and after'''

    before_dropping_duplicates = df.shape

    df = df.drop_duplicates()

    after_dropping_duplicates = df.shape

    retrun before_dropping_duplicates - after_dropping_duplicates, 'rows have been dropped!'



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


def add_language_column(column, df):

    '''this function returns a column identifying the language of the input column''' 

    language = []   

    for i in df[f'{column}']:
        if isinstance(i, float):
            language.append(0)
        else:
            a = langid.classify(i)
            language.append(a[0])

    df[f'{column}' + '_language'] = language

    return df




 












