from flight.logger import logging
from flight.exception import FlightException
from datetime import datetime
import os, sys

FILE_NAME = "flight.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):

        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y_%H%M%S')}")
        except Exception as e:
            logging.debug(str(e))
            raise FlightException(error_message=e, error_detail=sys)



class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        try:
            self.database_name = "flight_fare_prediction"
            self.collection_name = "flight_fare"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2

        except Exception as e:

            logging.debug(str(e))
            raise FlightException(error_message=e, error_detail=sys)


    def to_dict(self)->dict:

        try:
            return self.__dict__

        except Exception as e:
            logging.debug(str(e))
            raise FlightException(error_message=e, error_detail=sys)


class DataValidationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        try:

            self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
            self.report_file_path = os.path.join(self.data_validation_dir, "report.yaml")
            self.missing_threshold:float = 0.2
            self.base_file_path = os.path.join("Data_Train.xlsx")

        except Exception as e:

            logging.debug(str(e))
            raise FlightException(error_message=e, error_detail=sys)


class DataTransformationConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        try:

            self.useless_features = ["Route", "Additional_Info"]
            
            self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir, "data_transformation")
            self.transform_train_path = os.path.join(self.data_transformation_dir, "general_model",TRAIN_FILE_NAME)
            self.transform_test_path = os.path.join(self.data_transformation_dir, "general_model", TEST_FILE_NAME)

            self.JetAirways_train_path = os.path.join(self.data_transformation_dir, "JetAirways_model",TRAIN_FILE_NAME)
            self.JetAirways_test_path = os.path.join(self.data_transformation_dir, "JetAirways_model",TEST_FILE_NAME)

            self.Indigo_train_path = os.path.join(self.data_transformation_dir, "Indigo_model",TRAIN_FILE_NAME)
            self.Indigo_test_path = os.path.join(self.data_transformation_dir, "Indigo_model",TEST_FILE_NAME)

            self.AirIndia_train_path = os.path.join(self.data_transformation_dir, "AirIndia_model",TRAIN_FILE_NAME)
            self.AirIndia_test_path = os.path.join(self.data_transformation_dir, "AirIndia_model",TEST_FILE_NAME)

            self.MultipleCarriers_train_path = os.path.join(self.data_transformation_dir, "MultipleCarriers_model",TRAIN_FILE_NAME)
            self.MultipleCarriers_test_path = os.path.join(self.data_transformation_dir, "MultipleCarriers_model",TEST_FILE_NAME)

            self.SpiceJet_train_path = os.path.join(self.data_transformation_dir, "SpiceJet_model",TRAIN_FILE_NAME)
            self.SpiceJet_test_path = os.path.join(self.data_transformation_dir, "SpiceJet_model",TEST_FILE_NAME)

            self.Vistara_train_path = os.path.join(self.data_transformation_dir, "Vistara_model",TRAIN_FILE_NAME)
            self.Vistara_test_path = os.path.join(self.data_transformation_dir, "Vistara_model",TEST_FILE_NAME)

            self.AirAsia_train_path = os.path.join(self.data_transformation_dir, "AirAsia_model",TRAIN_FILE_NAME)
            self.AirAsia_test_path = os.path.join(self.data_transformation_dir, "AirAsia_model",TEST_FILE_NAME)

            self.GoAir_train_path = os.path.join(self.data_transformation_dir, "GoAir_model",TRAIN_FILE_NAME)
            self.GoAir_test_path = os.path.join(self.data_transformation_dir, "GoAir_model",TEST_FILE_NAME)


        except Exception as e:

            logging.debug(str(e))
            raise FlightException(error_message=e, error_detail=sys)



class ModelTrainingConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...