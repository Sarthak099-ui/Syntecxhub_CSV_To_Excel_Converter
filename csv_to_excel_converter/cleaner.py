import pandas as pd
from logger import logger

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting data cleaning...")
    if df.empty:
        return df
    df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip().replace(['nan', 'None', ''], 'N/A')
        else:
            df[col] = df[col].fillna(0)
    return df
