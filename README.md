# emailsender.github.io

Description:
The Email Sender GUI is a Python application that allows users to send emails through a graphical user interface (GUI). The application provides the following features:

Sender Email: Input field for the sender's email address.
Receiver Email: Input field for the recipient's email address.
Subject: Input field to specify the subject of the email.
Password: Input field for the sender's email password (Gmail users may need to use an App Password).
Message Body: A text area to compose the email body.
Send Email Button: A button to send the email after filling out the form.
The application uses the smtplib library for sending emails through a secure SSL connection (Gmail’s SMTP server is used by default). The email message is created using the MIMEText and MIMEMultipart classes from the email.mime module.

The improved design makes the interface more visually appealing with modern styling and layout features such as:

Structured form fields for easy input.
A prominent "Send Email" button.
Success and error messages to inform the user of the email sending status.


Instructions:
Download and Install Python:

Ensure that Python 3.x is installed on your computer. You can download it from python.org.
Save the Code:

Copy the provided Python code into a new file and save it as email_sender_gui.py.
Run the Application:

Open a terminal or command prompt on your computer.
Navigate to the directory where the file is saved.
Run the script by typing:
python email_sender_gui.py
Fill in the Email Details:

Sender Email: Enter the email address from which you want to send the email.
Receiver Email: Enter the recipient's email address.
Subject: Enter the subject line for the email.
Password: Enter the sender's email account password. (For Gmail users, use an App Password if two-factor authentication is enabled).
Message Body: Enter the body content of the email.
Click "Send Email":

After filling out the fields, click the Send Email button to send the email.
You will receive a success message if the email is sent successfully or an error message if something goes wrong (e.g., invalid email or incorrect credentials).

Requirements:
Python Version: The program requires Python 3.x.

You can download and install Python from python.org.
Required Libraries:

The required libraries are included with Python and do not need to be installed separately.
Tkinter: For creating the GUI (comes pre-installed with Python 3.x).
smtplib: For sending emails (comes with Python).
ssl: For creating a secure SSL connection (comes with Python).
email.mime: For composing the email message (comes with Python).
Email Account:

Sender's Email: You need a working email account from which you want to send emails. This example uses Gmail’s SMTP server by default (smtp.gmail.com).
App Password (Gmail): If you are using Gmail and have two-factor authentication (2FA) enabled, you will need to generate an App Password. You can generate it from your Google account settings.
Generate Google App Password
SMTP Server Details (For Gmail):

SMTP Server: smtp.gmail.com
SMTP Port (SSL): 465
For users with other email providers, you can adjust the SMTP server and port accordingly (e.g., for Outlook, Yahoo, etc.).
