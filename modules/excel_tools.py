#custom definitions to make data management with easier.
#modules: pandas
#cheat sheet: https://www.dataquest.io/blog/pandas-cheat-sheet/

def read_file(file_path, skiprows=0):
    #reads an xls or csv file and returns it as a dataframe.
    import pandas as pd
    
    #read .xls or .xlsx file
    if file_path[-4:] == '.xls' or file_path[-5:] == '.xlsx':
        dataframe = pd.read_excel(file_path, skiprows=skiprows)
    
    #read .csv file    
    elif file_path[-4:] == '.csv':
        dataframe = pd.read_csv(file_path, skiprows=skiprows)
    
    #read failure
    else:
        dataframe = "file must end with .xlx, .xlsx, .csv!"
        print(file_path, "is not a valid filepath!")
    
    #return the read dataframe
    return dataframe


def dataframe_cull_duplicates(dataframe, key, keep='first'):
    #delete duplicate rows under column specified by key.
    import pandas as pd
    
    dataframe_culled = dataframe.drop_duplicates(subset=[key], keep=keep)
    
    #return the culled dataframe
    return dataframe_culled


def dataframe_merge(dataframe_1, dataframe_2, merge_key):
    #merge two csv files based off of a shared key.
    import pandas as pd

    #merge dataframes together using common merge_key
    dataframe_merged = pd.merge(dataframe_1, dataframe_2, on=merge_key, how='outer')
    
    #return the merged csv
    return dataframe_merged


def file_export(dataframe, file_path):
    #exports a dataframe to .xls, .xlsx, or .csv
    import pandas as pd
        
    #export .xls or .xlsx file
    if file_path[-4:] == '.xls' or file_path[-5:] == '.xlsx':
        dataframe_export = dataframe.to_excel(file_path)
        print("Export Successful!")
    
    #export .csv file    
    elif file_path[-4:] == '.csv':
        dataframe_export = dataframe.to_csv(file_path)
        print("Export Successful!")
    
    #export failure
    else:
        dataframe = "exported file must end with .xlx, .xlsx, .csv!"
        print(file_path, "is not a valid filepath!/nExport failed")
    

################################################################################    
#EXECUTE
_1 = '/Users/christian.gentry/Downloads/new/geocoded_schools_clean_data_1.csv'
_2 = '/Users/christian.gentry/Downloads/new/ncesdata_B99FF9AD_condensed.xlsx'

new = read_file(_1)
old = read_file(_2)

_3 = dataframe_merge(new, old, 'input_string')

file_export(_3, '/Users/christian.gentry/Downloads/new/combined.csv')


