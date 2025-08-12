import pandas as pd 
import os
from datetime import datetime

def generate_weekly_report(cleaned_path):
    data_path = os.path.join('..', 'data', 'Superstore_cleaned.csv')
    df = pd.read_csv(data_path, parse_dates=['Order_Date'])

    df['Week'] = df['Order_Date'].dt.isocalendar().week
    df['Year'] = df['Order_Date'].dt.year

    weekly_report = df.groupby(['Year', 'Week', 'Region']).agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Quantity': 'sum'
    }).reset_index()

    weekly_report = weekly_report.sort_values(by=['Year', 'Week'])

    output_dir = 'outputs'   
    os.makedirs(output_dir, exist_ok=True)     

    today = datetime.now().strftime('%Y-%m-%d')
    output_filename = f'weekly_sales_report_{today}.xlsx'
    output_path = os.path.join(output_dir, output_filename)

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        weekly_report.to_excel(writer, index=False, sheet_name='Weekly Summary')

    print(f'Weekly report saved at: {output_path}')
    os.startfile(output_path)

    return output_path