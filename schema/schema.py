#schema files define the strucure of data and type of data,role book of data
#uses : 
#1. It ensures all rules to follow the same data structure
#2. It helps to validate and data cleaning
#3.Faster processing ,easier analytics(filtering,mapping,grouping ,anomaly detection becomes simple and fast)
log_schema = {
    "timestamp":"datetime",
    "level":"string",
    "service":"string",
    "message":"string",
}
#dataframe = df.astype(log_schema)