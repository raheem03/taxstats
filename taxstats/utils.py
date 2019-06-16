import win32com.client as win32
import pandas as pd
import os

def parse_docs(filename):
    """
    Take IRS SOI dictionary from .doc and converts to rectangular dataframe in
    CSV format
    """
    
    # open word doc
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(os.getcwd() + '/' + filename + ".doc")
    doc.Activate()
        
    # read word doc as list of lists
    data = [doc.Tables(i).Range.Text for i in range(1,5)]
    data = ''.join(data)
    data = data.replace('\r\x07\r\x07', ', ')
    data = data.replace('\r\x07', ', ')
    data = data.split(", ")
    
    # separate columns into lists
    varname = data[0::4]
    description = data[1::4]
    valuelineref = data[2::4]
    type = data[3::4]

    # create pandas dataframe and clean up
    df = pd.DataFrame(list(zip(varname, description, valuelineref, type)))
    doc.Close(True) # is this a function?
    headers = df.iloc[0]
    df = df[1:]
    df.columns = headers
    df['Variable Name'] = df['Variable Name'].str.replace('\r','')
        
    # store as csv
    df.to_csv(filename + '.csv', index = False)
    return df

def create_labels(filename):
    """
    Use IRS SOI dictionary in CSV format to create dictionary to serve as 
    labels
    """
    df = pd.read_csv(filename + '.csv')
    labels = pd.Series(df['Description'].values,index=df['Variable Name']).to_dict()
    return labels