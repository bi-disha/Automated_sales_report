import pandas as pd
import os
from datetime import datetime

def clean_data(data_path):
    data_path = r"E:\DATA ENGINEERING PROJECT\Automated_sales_report\data\Sample_Superstore.csv"
    df = pd.read_csv(data_path, encoding='latin1')

    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_')

    print("Shape:\n", df.shape)
    print("Columns:\n", df.columns)
    print("Sample data:\n", df.head())

    cleaned_dir = os.path.join('..', 'data')
    os.makedirs(cleaned_dir, exist_ok=True)
    cleaned_path = os.path.join(cleaned_dir, 'Superstore_cleaned.csv')
    df.to_csv(cleaned_path, index=False)

    return cleaned_path


