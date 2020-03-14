import pandas as pd
import numpy as np
import sys


schema2019 = pd.read_csv("data/raw data/developer_survey_2019/survey_results_schema.csv")


def get_desc(column_name, schema=schema2019):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT - 
            desc - string - the description of the column
    '''
    desc = list(schema[schema['Column'] == column_name]['QuestionText'])[0]
    return desc

def get_desc2(column_name, schema=schema2019):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT - 
            desc - string - the description of the column
    '''
    desc = list(schema[schema['Column'] == column_name]['QuestionText'])[0]
    return desc



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
