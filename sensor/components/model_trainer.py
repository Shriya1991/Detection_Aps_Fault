from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
from typing import Optional
import os,sys
from xgboost import XGBClassifier
from sensor import utils
from sklearn.metrics import f1_score

class ModelTrainer:
    
    def __init__(self,model_trainer_config:config_entity.ModelTrainerConfig, 
                     data_transformation_artifact: artifact_entity.DataTransformationArtifact):
                     try:
                        self.model_trainer_config = model_trainer_config
                        self.data_transformation_artifact = data_transformation_artifact
                     except Exception as e:
                        raise SensorException(e,sys)
    
    def fine_tune(self):
        try:
            pass
        except  Exception as e:
            raise SensorException(e,sys)

    def train_model(self, x,y):
        try:
            xgb_clf = XGBClassifier() 
            xgb_clf.fit(x,y)
            return xgb_clf
        except Exception as e:
            raise SensorException(e, sys)


    def initiate_model_trainer(self,)-> artifact_entity.ModelTrainerArtifact:
        try:
            logging.info(f"Loading train and test numpy array.")
            train_arr = utils.load_numpy_array(file_path=self.data_transformation_artifact.transform_train_path)
            test_arr = utils.load_numpy_array(file_path=self.data_transformation_artifact.transform_test_path)

            logging.info(f"Splitting input & target feature from both train and test array")
            x_train, y_train = train_arr[:, :-1], train_arr[:,-1]
            x_test, y_test = test_arr[:,:-1], test_arr[:,-1]

            logging.info(f"Train the model")
            model = self.train_model(x=x_train, y=y_train)

            logging.info(f"Calculate train f1 score")
            yhat_train = model.predict(x_train)
            f1_train_score = f1_score(y_true = y_train, y_pred = yhat_train) 

            logging.info(f"Calculate test f1 score")
            yhat_test = model.predict(x_test)
            f1_test_score = f1_score(y_true = y_test, y_pred= yhat_test)

            logging.info(f"train score: {f1_train_score} and test score:{f1_test_score}")
            #check for overfitting or underfitting or expected 
            logging.info("check if our model underfitting or not")
            if f1_train_score < self.model_trainer_config.expected_score:
                raise Exception(f"Model is not good as it is not able to give \
                expected accuracy :{self.model_trainer_config.expected_score:}: model actual score is {f1_train_score}")

            logging.info("Check if the model is overfitting or not")
            diff = f1_train_score - f1_test_score
            if diff > self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Train and Test f1 score difference : {diff} is more than Overfitting threshold {self.model_trainer_config.overfitting_threshold}")

            logging.info(f"save the training model")
            utils.save_object(file_path=self.model_trainer_config.model_path, obj= model)

            logging.info("Preparing the artifact")
            # prepare artifact
            model_trainer_artifact = artifact_entity.ModelTrainerArtifact(model_path = self.model_trainer_config.model_path, 
            f1_train_score = f1_train_score, f1_test_score = f1_test_score)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise SensorException(e, sys)
