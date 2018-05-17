import pandas as pd

def csv_merge(csv_1, csv_2, merge_key):
    #merge two csv files based off of a shared key.

    #create dataframes from imported csv files
    df1 = pd.read_csv(csv_1, skiprows=0)
    df2 = pd.read_csv(csv_2, skiprows=0)
    
    #recreate dataframes with headers identified
    df1 = pd.read_csv(csv_1, names=df1.columns.values, skiprows=1)
    df2 = pd.read_csv(csv_2, names=df2.columns.values, skiprows=1)

    #merge dataframes together using common merge_key
    df_merged = pd.merge(df1, df2, on=merge_key, how='outer')
    
    #cull any duplicates under the merge_key category.
    df_merged = df_merged.drop_duplicates(subset=[merge_key], keep='first')
    
    #return the merged dataframe
    return df_merged
    
    
    

'''
df1 = pd.read_csv('/Users/christian.gentry/Desktop/_1.csv')
 
print(df1.columns.values)
'''

df3 = csv_merge('/Users/christian.gentry/Desktop/_1.csv', '/Users/christian.gentry/Desktop/_2.csv', 'name' )

print(df3)
