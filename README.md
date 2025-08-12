# 🧾 Automated Sales Report with Python

This project automates the entire sales reporting process:
- Cleans raw sales data
- Generates weekly Excel reports
- Sends reports automatically via email (Gmail SMTP)

---

## 📁 Project Structure

AUTOMATED_SALES_REPORT/
│
├── data/
│ └── Sample_Superstore.csv # Raw input sales data
│
├── outputs/
│ └── weekly_sales_report_*.xlsx # Auto-generated reports
│
├── utils/
│ ├── init.py # Marks utils as a package
│ ├── cleaner.py # Data cleaning logic
│ ├── generate_report.py # Creates Excel reports
│ └── email_report.py # Sends email with report
│
├── main.py # Main script to run the whole pipeline
└── README.md # Project documentation



---

## 🚀 Features

- 📊 Reads raw sales data from `.csv`
- 🧹 Cleans and processes the data
- 📈 Generates a summary Excel report
- 📧 Automatically emails the report to a given address

---

## ⚙️ How to Use

1. Place your raw sales data in the `data/` folder.
2. Open `main.py` and configure your email credentials.
3. Run the script:
   ```bash
   python main.py


🔧 Requirements
Make sure to install the required Python libraries:

bash
Copy
Edit
pip install pandas openpyxl



🛠 Tech Stack
Python 3

pandas

openpyxl

smtplib

VS Code


🔐 Important Notes
If you're using your Gmail to send the report:

Enable App Passwords

Avoid hardcoding credentials directly into scripts

Instead, use environment variables or a .env file


🧪 Sample Output
The report is generated weekly and saved under the outputs/ folder as an Excel file.
Filename format: weekly_sales_report_YYYY-MM-DD.xlsx


✨ Author
Bidisha Pal
Final Year CSE Student | Data Engineering Enthusiast

