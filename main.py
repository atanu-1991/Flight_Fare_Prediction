from flight.logger import logging
from flight.exception import FlightException
from flight.utils import get_collection_as_dataframe
from flight.entity import config_entity
from flight.components.data_ingestion import DataIngestion
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

          training_pipeline_config = config_entity.TrainingPipelineConfig()

          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())

          data_ingestion = DataIngestion(data_ingestion_config= data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())

     except Exception as e:
          logging.debug(str(e))
          raise FlightException(e, sys)