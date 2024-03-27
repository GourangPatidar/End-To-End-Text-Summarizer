from textSummarizer.entity import DataIngestionConfig
from textSummarizer.components.data_ingestion import DataIngestion 
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main (self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            Data_ingestion=DataIngestion(config=data_ingestion_config)
            Data_ingestion.download_file()
            Data_ingestion.extract_zip_file()
        except Exception as e:
            raise e