import pandas as pd
import numpy as np
import sys
from zipfile import ZipFile

schema2019 = pd.read_csv("data/raw data/developer_survey_2019/survey_results_schema.csv")

# load 2019 survey results (if not already loaded)
try:
    df
except NameError:
    df = load_csv("data/raw data/developer_survey_2019/survey_results_public.csv.zip")
    


def load_csv(file):
    '''
    INPUT - file - string - path of csv file (zipped or unzipped)
    OUTPUT - df - pandas dataframe
    '''
    # if regular csv-file:
    if file.endswith('.csv'):
        df = pd.read_csv(file)
        
    # if zip-file:
    else:
        zip_file = ZipFile(file)
        df = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename)) 
              for text_file in zip_file.infolist() if text_file.filename.endswith('.csv')}
        df = df["survey_results_public.csv"]    
    
    return df


def get_desc(column_name, schema=schema2019):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT - 
            desc - string - the description of the column
    '''
    desc = list(schema[schema['Column'] == column_name]['QuestionText'])[0]
    
    return desc


def get_cat(column_name, df=df):
    '''
    INPUT - column_name - string - the categories column name you want to know about
          - df - pandas dataframe
    OUTPUT - 
            cat - list - categories of this variable
    '''
    
    if df[column_name].dtype=="object":
        return list(df[column_name].unique())
    else:
        return mean(df[column_name])


def df_info(df):
    '''
    INPUT - df - pandas dataframe
    OUTPUT - None
    '''
    print("Rows: {} \t Variables: {} \t \t Size: {} kb".format(
        df.shape[0], 
        df.shape[1],
        "n/a" #sys.getsizeof(df)/1024
    )
         )
    
    return None
