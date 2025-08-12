import os
from utils.cleaner import clean_data
from utils.generate_report import generate_weekly_report
from utils.email_report import send_email
import getpass

data_path = r"E:\DATA ENGINEERING PROJECT\Automated_sales_report\data\Sample_Superstore.csv"

if __name__ == "__main__":
    sender_email = input("Enter sender email: ")
    sender_password = getpass.getpass("Enter sender email password: ")
    recipient_email = input("Enter recipient email: ")
    cleaned_path = clean_data(data_path)
    report_path = generate_weekly_report(cleaned_path)
    send_email(report_path, sender_email, sender_password, recipient_email)
