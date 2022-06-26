import pandas as pd

def hello():
    """Print hello, world to demonstrate use of the source library."""
    print("Hello, World")
    return

def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')

def split_name(x_df):
    def split_name_series(string):
        firstName, secondName=string.split(', ')
        return pd.Series(
            (firstName, secondName),
            index='firstName secondName'.split()
        )
    # Select the Name column and apply a function
    res=x_df['Name'].apply(split_name_series)
    x_df[res.columns]=res
    return x_df

def substitute_sex(x_df):
    mapping={'male':'M','female':'F'}
    x_df['Sex']=x_df['Sex'].map(mapping)
    return x_df

def replace_age_na(x_df, fill_map):
    '''Replace the missing Age with some form of imputation'''
    cond=x_df['Age'].isna()
    res=x_df.loc[cond,'Pclass'].map(fill_map)
    x_df.loc[cond,'Age']=res
    return x_df

