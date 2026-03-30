#whuch is used to handle the data and reusable code which is seperate from the dask
#loading the data
#parsing the data
#structure the data and load the data using injection files 
#parser: It is a python method which is used to convert raw data into structured data based on 
#the schema which we have defined (translator) 
# Without parser: No columns are defined
#no filtering is done
#no anamoly is detection or no aggregation
#with parsing: we can filter error logs
#detect the unusual patterns 
#it converts raw log data to the machine readable language
#loader is to inject the log data into the file

import dask.bag as db
from injection.parser import parse_log_line
from schema.schema import log_schema

def load_logs(file_path):
    bag = db.read_text(file_path)
    return bag
    #return df.astype(log_schema)
    #return df 