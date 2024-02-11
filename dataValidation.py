import logging as logger
import sys
from unziputility import UnzipUtility

logger.basicConfig(filename='app.log', level=logger.DEBUG, format='%(asctime)s - %(message)s')


def main():
    input_folder_path = sys.argv[1]
    extracted_folder_path = sys.argv[2]

    unziputility = UnzipUtility()
    # Call the function to unzip files in the folder
    unziputility.unzip_files(input_folder_path, extracted_folder_path)
    # call the function for the validation
    unziputility.validation(input_folder_path, extracted_folder_path)


if __name__ == "__main__":
    main()
