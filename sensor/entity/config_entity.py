import os
from datetime import datetime


FILE_NAME = "sensor.csv"

class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir = od.path.join(os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y_%H%M%S')}")

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.database_name="aps"
        self.collection_name="sensor"
        self.data_ingestion_dir= os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
        self.feature_store_dir = os.path.join(self.data_ingestion_dir,"")
        
class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...


