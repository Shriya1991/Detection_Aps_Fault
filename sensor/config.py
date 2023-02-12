import pymongo
import pandas as pd 
import json
from dataclasses import dataclass

#provide the MongoDB localhost url to connect python to MongoDB
import os
@dataclass
class EnvironmentVariable:
    mongo_db_url:str=os.getenv("MONGO_DB_URL")
    aws_access_key_id:str=os.getenv("AWS_ACCESS_KEY_ID")
    aws_acess_secret_key:str=os.getenv("AWS_ACESS_SECRET_KEY")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)