import tkinter as tk
from tkinter import messagebox
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email():
    # Get values from entry fields
    sender_email = sender_email_entry.get()
    receiver_email = receiver_email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", "end-1c")
    password = password_entry.get()

    if not sender_email or not receiver_email or not subject or not body or not password:
        messagebox.showwarning("Input Error", "Please fill all the fields.")
        return

    try:
        # Set up the email server (Gmail's SMTP server)
        smtp_server = "smtp.gmail.com"
        smtp_port = 465

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add the body to the email message
        message.attach(MIMEText(body, "plain"))

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        # Show success message
        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

# Create the main window
root = tk.Tk()
root.title("Email Sender")

# Set the window size and background color
root.geometry("500x550")
root.config(bg="#f4f4f4")

# Add a title label
title_label = tk.Label(root, text="Email Sender", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

# Create a frame for input fields to keep the layout organized
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

# Sender Email Label and Entry
tk.Label(frame, text="Sender Email:", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, padx=10, pady=5, sticky="w")
sender_email_entry = tk.Entry(frame, width=35, font=("Arial", 12), bd=2, relief="solid")
sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

# Receiver Email Label and Entry
tk.Label(frame, text="Receiver Email:", font=("Arial", 12), bg="#f4f4f4").grid(row=1, column=0, padx=10, pady=5, sticky="w")
receiver_email_entry = tk.Entry(frame, width=35, font=("Arial", 12), bd=2, relief="solid")
receiver_email_entry.grid(row=1, column=1, padx=10, pady=5)

# Subject Label and Entry
tk.Label(frame, text="Subject:", font=("Arial", 12), bg="#f4f4f4").grid(row=2, column=0, padx=10, pady=5, sticky="w")
subject_entry = tk.Entry(frame, width=35, font=("Arial", 12), bd=2, relief="solid")
subject_entry.grid(row=2, column=1, padx=10, pady=5)

# Password Label and Entry
tk.Label(frame, text="Password (for sender's email):", font=("Arial", 12), bg="#f4f4f4").grid(row=3, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(frame, width=35, font=("Arial", 12), bd=2, relief="solid", show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

# Message Body Label and Text Box
tk.Label(root, text="Message Body:", font=("Arial", 12), bg="#f4f4f4").pack(pady=5)
body_text = tk.Text(root, width=45, height=10, font=("Arial", 12), bd=2, relief="solid")
body_text.pack(pady=5)

# Send Email Button with a customized style
send_button = tk.Button(root, text="Send Email", command=send_email, width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), bd=0, relief="flat")
send_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
