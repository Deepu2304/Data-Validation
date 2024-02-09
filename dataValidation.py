import logging
import zipfile
import logging as logger
import os
import sys


logger.basicConfig(filename='app.log', level=logger.DEBUG, format='%(asctime)s - %(message)s')


def unzip_files(input_folder_path, extracted_folder_path):
    # List all files in the folder
    logger.info(f"reading files in the {input_folder_path}")
    files = os.listdir(input_folder_path)

    # Iterate through each file
    for file in files:
        file_path = os.path.join(input_folder_path, file)
        logging.info("searching through the folder for zip file")

        # Check if the file is a zip file
        if zipfile.is_zipfile(file_path):
            logger.info("checking weather the file is zip or not ")
            # Create a subdirectory within the extract folder with the same name as the zip file
            extract_subdirectory = os.path.join(extracted_folder_path, os.path.splitext(os.path.basename(file))[0])
            os.makedirs(extract_subdirectory, exist_ok=True)

            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                logger.info(f"exporting the files to the {extract_subdirectory}")
                zip_ref.extractall(extract_subdirectory)
                logging.info(f"succesfully exported the the unzipped files to the {extract_subdirectory}")
        else:
            print(f"{file} is not a zip file")


def validation(input_folder_path, extracted_folder_path):
    logger.info("validating files")
    input_files = os.listdir(input_folder_path)
    logger.info(f"working on the count of zip files in {input_folder_path}")
    zipfile_count = sum(1 for file in input_files if zipfile.is_zipfile(os.path.join(input_folder_path, file)))
    logger.info(f"working on the count of extracted files in {extracted_folder_path}")
    extractedfile_count = sum(len(files) for _, _, files in os.walk(extracted_folder_path))
    print(f"zipcount is {zipfile_count}")
    print(f"extractcount is {extractedfile_count}")
    # print(os.listdir(extracted_folder_path))
    logger.info("checking conditions for validation")
    if zipfile_count == extractedfile_count:
        print("all the zip files were successfully extracted")
    else:
        print("the No: of extracted files is not match with the zip files")


def main():
    input_folder_path = '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/source-data'
    extracted_folder_path = '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/extracted-data'

    # Call the function to unzip files in the folder
    unzip_files(input_folder_path, extracted_folder_path)
    # call the function for the validation
    validation(input_folder_path, extracted_folder_path)


if __name__ == "__main__":
    main()
