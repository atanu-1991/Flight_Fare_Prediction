import pymongo
import pandas as pd
import json

from flight.config import mongo_client


# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "E:\FullStack_Data_Science_Bootcamp\DOWNLOAD_PROJECT\Flight_Fare_Prediction\Data_Train.xlsx"
DATABASE_NAME = "flight_fare_prediction"
COLLECTION_NAME = "flight_fare"


if __name__ == "__main__":
    df = pd.read_excel(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    # Convert data frame to json format so that we can dump this record into mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # insert converted json record to mong db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

