# Automated_sales_report
Python automation project to clean sales data, generate weekly Excel reports, and email them using Gmail

🧾 Automated Sales Report with Python
This project automates the entire sales reporting process:

🧹 Cleans raw sales data

📈 Generates weekly Excel reports

📧 Sends reports automatically via email using Gmail SMTP

📁 Project Structure
AUTOMATED_SALES_REPORT/
│
├── data/
│   └── Sample_Superstore.csv         # Raw input sales data
│
├── outputs/
│   └── weekly_sales_report_*.xlsx    # Auto-generated reports
│
├── utils/
│   ├── __init__.py                   # Marks utils as a package
│   ├── cleaner.py                    # Data cleaning logic
│   ├── generate_report.py            # Creates Excel reports
│   └── email_report.py               # Sends email with report
│
├── main.py                           # Main script to run the whole pipeline
└── README.md                         # Project documentation

🚀 Features
📊 Reads raw sales data from .csv

🧼 Cleans and processes the data

📈 Generates a weekly summary Excel report

📧 Automatically emails the report to a recipient

⚙️ How to Use
Place your raw sales data in the data/ folder.

Open main.py and configure your Gmail credentials securely.

Run the pipeline:

python main.py
🔧 Requirements
Install the required libraries before running the script:


pip install pandas openpyxl
🛠 Tech Stack
Python 3

pandas

openpyxl

smtplib

VS Code

🔐 Important Notes
If you're using Gmail to send reports:

Enable App Passwords in your Google account settings.

Avoid hardcoding credentials into the script.

Use environment variables or a .env file for storing sensitive information.

🧪 Sample Output
The report is generated weekly and saved in the outputs/ folder.
Filename format:

weekly_sales_report_YYYY-MM-DD.xlsx
✨ Author
Bidisha Pal
Final Year CSE Student | Data Engineering Enthusiast


