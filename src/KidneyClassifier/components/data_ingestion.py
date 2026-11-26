import os
import zipfile
import gdown
from pathlib import Path
from KidneyClassifier import logger
from KidneyClassifier.utils.common import get_size
from KidneyClassifier.entity.config_entity import DataIngestionConfig




class DataIngestion:

    def __init__(self, config):
        self.config = config

    def download_file(self) -> str:

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file

            os.makedirs(self.config.root_dir, exist_ok=True)

            if not os.path.exists(zip_download_dir):

                logger.info(
                    f"Downloading data from {dataset_url} "
                    f"into file {zip_download_dir}"
                )

                file_id = dataset_url.split("/")[-2]

                prefix = "https://drive.google.com/uc?export=download&id="

                gdown.download(
                    prefix + file_id,
                    str(zip_download_dir),
                    quiet=False
                )

                logger.info(
                    f"Downloaded data from {dataset_url} "
                    f"into file {zip_download_dir}"
                )

            else:
                logger.info(
                    f"File already exists with size: "
                    f"{get_size(Path(zip_download_dir))}"
                )

        except Exception as e:
            raise e

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(
            self.config.local_data_file, "r"
        ) as zip_ref:

            zip_ref.extractall(unzip_path)

        logger.info(
            f"Extracted ZIP file into directory: {unzip_path}"
        )


