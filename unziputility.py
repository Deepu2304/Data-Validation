import zipfile
import logging as logger
import os


class UnzipUtility:
    def unzip_files(self, input_folder_path, extracted_folder_path):
        # List all files in the folder
        logger.info(f"reading files in the {input_folder_path}")
        files = os.listdir(input_folder_path)
        os.makedirs(extracted_folder_path, exist_ok=True)

        # Iterate through each file
        for file in files:
            file_path = os.path.join(input_folder_path, file)
            logger.info("searching through the folder for zip file")

            # Check if the file is a zip file
            if zipfile.is_zipfile(file_path):
                logger.info("checking weather the file is zip or not ")
                # Create a subdirectory within the extract folder with the same name as the zip file
                extract_subdirectory = os.path.join(extracted_folder_path, os.path.splitext(os.path.basename(file))[0])
                os.makedirs(extract_subdirectory, exist_ok=True)

                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    logger.info(f"exporting the files to the {extract_subdirectory}")
                    zip_ref.extractall(extract_subdirectory)
                    logger.info(f"succesfully exported the the unzipped files to the {extract_subdirectory}")
            else:
                print(f"{file} is not a zip file")

    def validation(self, input_folder_path, extracted_folder_path):
        logger.info("validating files")
        input_files = os.listdir(input_folder_path)
        logger.info(f"working on the count of zip files in {input_folder_path}")
        zipfile_count = sum(1 for file in input_files if zipfile.is_zipfile(os.path.join(input_folder_path, file)))
        logger.info(f"working on the count of extracted files in {extracted_folder_path}")
        logger.info("counting number of extracted files")
        extractedfile_count = len([name for name in os.listdir(extracted_folder_path) if
                                   os.path.isdir(os.path.join(extracted_folder_path, name))])
        print(f"zipcount is {zipfile_count}")
        print(f"extracted_zip_count is {extractedfile_count}")
        # print(os.listdir(extracted_folder_path))
        logger.info("checking conditions for validation")
        if zipfile_count == extractedfile_count:
            print("all the zip files were successfully extracted")
        else:
            print("the No: of extracted files is not match with the zip files")
