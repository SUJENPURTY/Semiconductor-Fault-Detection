
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://datasciencelearning7:Sujen2003@cluster0.y5cqkls.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

## create the database name and collectionn name
DATABASE_NAME = "purty"
COLLECTION_NAME = "waferfault"

## read the data as a dataframe
df = pd.read_csv(r"C:\Users\sujen\OneDrive\Desktop\Ad_project\ML_Project\Semiconductor-Fault-Detection\Notebook\Data\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0",axis=1)

## convert the data into json
json_records=list(json.loads(df.T.to_json()).values())

## now dump the data into the database

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)

