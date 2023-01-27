from flight.logger import logging
from flight.exception import FlightException
from flight.utils import get_collection_as_dataframe
from flight.entity import config_entity
from flight.components.data_ingestion import DataIngestion
from flight.components.data_validation import DataValidation

import sys,os

def test_logger_and_exception():
     try:
          logging.info("Starting the test_logger_and_exception")
          result = 3/0
          print(result)
          logging.info("Stopping the test_logger_and_exception")
          
     except Exception as e:
          logging.debug(str(e))
          raise FlightException(e, sys)


if __name__ == "__main__":
     try:
          # test_logger_and_exception()
          # get_collection_as_dataframe(database_name="flight_fare_prediction", collection_name="flight_fare")

          # Training Pipeline
          training_pipeline_config = config_entity.TrainingPipelineConfig()

          # Data Ingestion
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          # print(data_ingestion_config.to_dict())

          data_ingestion = DataIngestion(data_ingestion_config= data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

          # Data Validation
          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)

          data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
          data_validation_artifact = data_validation.initiate_data_validation()
          print(data_validation_artifact)

     except Exception as e:
          logging.debug(str(e))
          raise FlightException(e, sys)