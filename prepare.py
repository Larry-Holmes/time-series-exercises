import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt


def covert_date(df, col,fmat):
    df[col] = df[col].str.replace('00:00:00 GMT', '')
    df[col] = df[col].str.strip()
    df[col] = pd.to_datetime(df[col], format=fmat)
    
    return df


def plot_hist(df):
    
    for col in df.columns:
        df[col].hist().plot()
        plt.title(col)
        plt.show()
    
    

def date_index(df, col):
    
    df = df.set_index(col).sort_index()
    
    return df

def month_year_add(df):
    
    df['month'] = df.index.month_name()
    
    df['year'] = df.index.year
    
    return df

def prep_data(df):
    
    if df.isnull().any() == True:
        
        df.asfreq('d', method='ffill')
    
    else:
        
        print('no nulls!')

        

    
    