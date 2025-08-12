import smtplib 
from email.message import EmailMessage
import os
from datetime import datetime

#EMAIL_ADDRESS = 'bidishapal84@gmail.com'
#EMAIL_PASSWORD = 'qxfb rxod gpmz bnqy'

def send_email(report_path, sender_email,sender_password,recipient_email):
     today = datetime.now().strftime('%Y-%m-%d')
     report_filename = f'weekly_sales_report_2025-08-02.xlsx'
     report_path = os.path.join('outputs', report_filename)  

     print("Looking for report at:", os.path.abspath(report_path))

     msg = EmailMessage()
     msg['Subject'] ='Automated Weekly Sales Report'
     msg['From'] = sender_email
     msg['To'] = recipient_email
     msg.set_content(
     "Hi Rohit,\n\n"
     "I'm testing an automated report mailing script as part of my data engineering project.\n"
     "It includes a weekly sales report as an attachment.\n\n"
     "Please ignore the contents — it's just for testing.\n\n"
     "Thanks for helping me test this!\n\n"
     "Best Regards,\nBidisha"
     )

     with open(report_path,'rb') as f:
          file_data =f.read()
          msg.add_attachment(file_data, maintype ='application' , subtype ='vnd.openxmlformats_officedocument.spreadsheetml.sheet',filename = report_filename)

     with smtplib.SMTP_SSL ('smtp.gmail.com',465) as smtp:
          smtp.login(sender_email, sender_password)
          smtp.send_message(msg)

     print("Email sent successfully !")     

     