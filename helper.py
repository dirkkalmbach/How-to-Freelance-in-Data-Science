import pandas as pd
import numpy as np
import sys
from zipfile import ZipFile

schema2019 = pd.read_csv("data/raw data/developer_survey_2019/survey_results_schema.csv")


def load_csv_zip(year=2019):
    '''
    INPUT - year - int - year of the survey
    OUTPUT - df - pandas dataframe
    '''
    file = "data/raw data/{} Stack Overflow Survey Responses.csv.zip".format(str(year))

    zip_file = ZipFile(file)
    df = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename)) 
          for text_file in zip_file.infolist() if text_file.filename.endswith('.csv')}
    df = df["{} Stack Overflow Survey Responses.csv".format(str(year))]
    print("'{} Stack Overflow Survey Responses.csv' sucessfully loaded.".format(year))
    print("Rows: {} \t Variables: {}".format(df.shape[0], df.shape[1]))
    
    return df


def get_desc(column_name, year=2019):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT - 
            desc - string - the description of the column
    '''
    schema = "data/raw data/developer_survey_{}/survey_results_schema.csv".format(str(year))
    schema = pd.read_csv(schema)
    desc = list(schema[schema['Column'] == column_name]['QuestionText'])[0]
    
    print(desc)


def get_cat(column_name, df):
    '''
    INPUT - column_name - string - the categories column name you want to know about
          - df - dataframe 
    OUTPUT - 
            cat - list - categories of this variable
    ''' 
    if df[column_name].dtype=="object":
        print("Categories of {}:\n".format(column_name))
        for i in list(df[column_name].unique()):
              print(i)
    else:
        print("Mean of {}:\n{}".format(column_name, round(df[column_name].mean(),2) ))

    
def outlier(df, columns=None):
    """
    INPUT: columns - list of column names
           df - dataframe
    OUTPUT: df - Dataframe with eliminated Outliers
    """
    # if only df in argument extact all columns of df
    if columns==None:
        columns=df.columns
        
    print("old shape: {}".format(df.shape))
    count = 0
    i= 0 
    
    for var in columns:
        
        if df[var].dtype in ("int64","float64"): 
            #only outliers in numbers
            q1 = df[var].quantile(0.25)
            q3 = df[var].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 -(1.5 * iqr) 
            upper_bound = q3 +(1.5 * iqr)
            outliers = (df[var]<lower_bound) |  (df[var]>upper_bound)
            n_outliers = outliers.sum()
            
            #for info printout
            if n_outliers>0:
                print("\t💣💥 detected and eliminated {} outliers in col {}.".format(n_outliers,var))
                count += n_outliers
                i += 1
            df = df[~outliers] #eliminate all rows with outliers of this column from df
        else:
            pass
        
    print("new shape: {}".format(df.shape))  
    print("👉🏼 {} Outlier(s) in {} column(s) detected and eliminated.".format(count, i))
    
    return df





    