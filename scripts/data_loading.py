import pandas as pd
import os
import glob


def load_data(folder_name):
    try:
        # Get the current directory of the script
        script_dir = os.path.dirname(__file__)

        # Construct the relative path to the CSV file
        data_path = os.path.join(script_dir, '..', '..', 'Data')

        file_paths=glob.glob(os.path.join(data_path,folder_name,'*.csv'))

        if not file_paths:
            raise ValueError(f"No CSV files found in the 'data/{folder_name}' directory.")
        
        # Read the CSV file using pandas
        df_list = [pd.read_csv(file) for file in file_paths]
        data = pd.concat(df_list, ignore_index=True)
        # Number format to two decimal
        pd.set_option('display.float_format', '{:.2f}'.format)
        return data
    except FileNotFoundError as e:
        print(f"Error: Folder Data/{folder_name} was not found. Details: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: Folder Data/{folder_name} is empty. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred. Details: {e}")