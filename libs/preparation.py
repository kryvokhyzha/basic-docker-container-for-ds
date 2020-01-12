from libs import *


def fix_participation(column, char='%'):
    return column.apply(lambda cells: cells.strip(char))

def get_duplicate_rows(df):
    return df[df.duplicated()]

def remove_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    return df[~((df < (Q1 - 1.5*IQR)) | (df > (Q3 + 1.5*IQR))).any(axis=1)]