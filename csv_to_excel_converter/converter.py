import os
import pandas as pd
from logger import logger
from cleaner import clean_data

def convert_csv_to_excel(csv_path: str, excel_path: str) -> bool:
    if not os.path.exists(csv_path):
        logger.error(f"File not found: '{csv_path}'")
        return False
    try:
        df = pd.read_csv(csv_path)
        cleaned_df = clean_data(df)
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            cleaned_df.to_excel(writer, sheet_name='Cleaned Data', index=False)
        return True
    except Exception as e:
        logger.critical(f"Error: {str(e)}")
        return False
