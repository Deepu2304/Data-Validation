import zipfile
# unzip module is a built in module
import os


# function to unzip the files
def unzip_files(zip_file_paths, extracted_path):
    for zip_file in zip_file_paths:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # using this command we can extracted file with the name same as zip file
            extract_subfolder = os.path.join(extracted_path, os.path.splitext(os.path.basename(zip_file))[0])
            os.makedirs(extract_subfolder, exist_ok=True)
            zip_ref.extractall(extract_subfolder)


def main():
    # list of zip_file paths
    zip_file_paths = ['/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/British Airways.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Entertainment.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Finanace.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Health Care.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Government.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Education.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Agriculture.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Salaries.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/RealEstate.zip',
                      '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/Automobile.zip'
                      ]
    # the path for the extracted files to store
    extracted_path = '/Users/jaideepsai/Desktop/DATA-ANALYTICS/Data Source/extracts'

    unzip_files(zip_file_paths, extracted_path)


if __name__ == "__main__":
    main()
