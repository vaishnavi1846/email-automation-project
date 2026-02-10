
# import os
# import csv
# import smtplib
# import json
# from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
# from dotenv import load_dotenv
# from werkzeug.utils import secure_filename
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER", "static/uploads")
# app.secret_key = "supersecretkey"

# # Ensure upload folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# # Function to send email
# def send_email(name, recipient, subject, message, attachment=None):
#     try:
#         sender_email = os.getenv("EMAIL_USER")
#         sender_password = os.getenv("EMAIL_PASS")
#          # Ensure required fields are not empty
#         if not sender_email or not sender_password:
#             flash("Email credentials are missing!", "danger")
#             return

#         if not recipient or not subject or not message:
#             flash("Recipient, Subject, and Message are required!", "danger")
#             return

#         msg = MIMEMultipart()
#         msg['From'] = sender_email
#         msg['To'] = recipient
#         msg['Subject'] = subject
#         msg.attach(MIMEText(message, 'plain'))

#         msg.attach(MIMEText(message, 'plain'))

#         # Attach file if exists
#         if attachment:
#             try:
#                 with open(attachment, "rb") as file:
#                     part = MIMEBase("application", "octet-stream")
#                     part.set_payload(file.read())
#                     encoders.encode_base64(part)
#                     part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment)}")
#                     msg.attach(part)
#             except Exception as e:
#                 flash(f"Attachment Error: {str(e)}", "warning")
#         # Send email
#         server = smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT")))
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, recipient, msg.as_string())
#         server.quit()
        
#         flash(f"Email sent successfully to {recipient}!", "success")

#     except Exception as e:
#         flash(f"Failed to send email: {str(e)}", "danger")

# # Function to read emails from CSV
# def load_csv_data():
#     email_data = []
#     csv_file = "emails.csv"
    
#     if os.path.exists(csv_file):
#         with open(csv_file, newline="", encoding="utf-8") as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                  if row and row["Name"] and row["Recipient"] and row["Subject"]:
#                     email_data.append({
#                         "name": row["Name"].strip(),
#                         "recipient": row["Recipient"].strip(),
#                         "subject": row["Subject"].strip(),
#                         "message": row.get("Message", "").strip(),  # ✅ Extracting the message
#                         "attachment": row.get("Attachment","").strip() 
#                     })
                    
    
#     return email_data 

# @app.route("/", methods=["GET", "POST"])
# def index():
#     email_data = load_csv_data() 
#     print("Email Data Loaded:", email_data)  # Debugging line

#     return render_template("index.html", email_data=email_data or [])  # Ensure it's not None
# @app.route("/uploads/<filename>")
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
# @app.route("/send_email", methods=["POST"])
# def send():
#     name= request.form.get("name")
#     recipient = request.form.get("recipient")
#     subject = request.form.get("subject")
#     message = request.form.get("message")

#     # Handle file upload
#     attachment_path = None
#     if "attachment" in request.files:
#         file = request.files["attachment"]
#         if file.filename != "":
#             filename = secure_filename(file.filename)
#             attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(attachment_path)

#     return redirect(url_for("index"))
# @app.route("/send_bulk_email", methods=["POST"])
# def send_bulk_email():
#     email_data = load_csv_data()

#     if not email_data:
#         flash("No email data found in CSV!", "danger")
#         return redirect(url_for("index"))

#     for entry in email_data:
#         name = entry.get("name", "User")
#         recipient = entry.get("recipient")
#         subject = entry.get("subject")
#         message = entry.get("message", "No message provided.")
#         attachment = entry.get("attachment", "").strip()

#         # Check if attachment exists
#         attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], attachment) if attachment else None
#         if attachment and not os.path.exists(attachment_path):
#             attachment_path = None  # Ignore missing attachments

#         send_email(name, recipient, subject, message, attachment_path)

#     return redirect(url_for("index"))


# if __name__ == "__main__":
#     app.run(debug=True)

# import os
# import csv
# import smtplib
# import json
# from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
# from dotenv import load_dotenv
# from werkzeug.utils import secure_filename
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER", "static/uploads")
# app.secret_key = "supersecretkey"

# # Ensure upload folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# # Function to send email
# def send_email(name, recipient, subject, message, attachment=None):
#     try:
#         sender_email = os.getenv("EMAIL_USER")
#         sender_password = os.getenv("EMAIL_PASS")
        
#         if not sender_email or not sender_password:
#             flash("Email credentials are missing!", "danger")
#             return

#         if not recipient or not subject or not message:
#             flash("Recipient, Subject, and Message are required!", "danger")
#             return

#         msg = MIMEMultipart()
#         msg['From'] = sender_email
#         msg['To'] = recipient
#         msg['Subject'] = subject
#         msg.attach(MIMEText(message, 'plain'))

#         # Attach file if exists
#         if attachment:
#             try:
#                 with open(attachment, "rb") as file:
#                     part = MIMEBase("application", "octet-stream")
#                     part.set_payload(file.read())
#                     encoders.encode_base64(part)
#                     part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment)}")
#                     msg.attach(part)
#             except Exception as e:
#                 flash(f"Attachment Error: {str(e)}", "warning")

#         # Send email
#         server = smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT")))
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, recipient, msg.as_string())
#         server.quit()
        
#         flash(f"Email sent successfully to {recipient}!", "success")

#     except Exception as e:
#         flash(f"Failed to send email: {str(e)}", "danger")

# # Function to read emails from CSV
# def load_csv_data():
#     email_data = []
#     csv_file = "emails.csv"
    
#     if os.path.exists(csv_file):
#         with open(csv_file, newline="", encoding="utf-8") as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 if row and row["Name"] and row["Recipient"] and row["Subject"]:
#                     email_data.append({
#                         "name": row["Name"].strip(),
#                         "recipient": row["Recipient"].strip(),
#                         "subject": row["Subject"].strip(),
#                         "message": row.get("Message", "").strip(),
#                         "attachment": row.get("Attachment", "").strip()
#                     })
    
#     return email_data

# @app.route("/", methods=["GET", "POST"])
# def index():
#     email_data = load_csv_data()
#     print("Email Data Loaded:", email_data)

#     return render_template("index.html", email_data=email_data)

# @app.route("/uploads/<filename>")
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route("/send_email", methods=["POST"])
# def send():
#     name = request.form.get("name")
#     recipient = request.form.get("recipient")
#     subject = request.form.get("subject")
#     message = request.form.get("message")

#     # Handle file upload
#     attachment_path = None
#     if "attachment" in request.files:
#         file = request.files["attachment"]
#         if file.filename != "":
#             filename = secure_filename(file.filename)
#             attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(attachment_path)

#     #  Fix: Call send_email function
#     send_email(name, recipient, subject, message, attachment_path)

#     return redirect(url_for("index"))

# @app.route("/send_bulk_email", methods=["POST"])
# def send_bulk_email():
#     email_data = load_csv_data()

#     if not email_data:
#         flash("No email data found in CSV!", "danger")
#         return redirect(url_for("index"))

#     for entry in email_data:
#         name = entry.get("name", "User")
#         recipient = entry.get("recipient")
#         subject = entry.get("subject")
#         message = entry.get("message", "No message provided.")
#         attachment = entry.get("attachment", "").strip()

#         # Check if attachment exists
#         attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], attachment) if attachment else None
#         if attachment and not os.path.exists(attachment_path):
#             attachment_path = None  # Ignore missing attachments

#         send_email(name, recipient, subject, message, attachment_path)

#     return redirect(url_for("index"))

# if __name__ == "__main__":
#     app.run(debug=True)

# import os
# import csv
# import smtplib
# import re
# from pathlib import Path
# from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
# from dotenv import load_dotenv
# from werkzeug.utils import secure_filename
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders

# # Load .env file from project root (absolute path)
# load_dotenv(Path('.') / '.env')

# # Initialize Flask app
# app = Flask(__name__)

# # Configure from .env with fallbacks
# app.config.update(
#     UPLOAD_FOLDER=os.getenv("UPLOAD_FOLDER", "static/uploads"),
#     SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret-key-123"),
#     MAX_CONTENT_LENGTH=5 * 1024 * 1024  # 5MB file limit
# )

# # Ensure upload folder exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # Allowed file extensions
# ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}

# # Helper functions
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def is_valid_email(email):
#     return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# def send_email(name, recipient, subject, message, attachment=None):
#     try:
#         # Get credentials from .env
#         sender_email = os.getenv("EMAIL_USER")
#         sender_password = os.getenv("EMAIL_PASS")
#         smtp_host = os.getenv("EMAIL_HOST")
#         smtp_port = int(os.getenv("EMAIL_PORT", 587))
        
#         # Validate required fields
#         if not all([sender_email, sender_password, smtp_host]):
#             flash("Email server configuration is missing!", "danger")
#             return False

#         # Create email
#         msg = MIMEMultipart()
#         msg['From'] = sender_email
#         msg['To'] = recipient
#         msg['Subject'] = subject
#         msg.attach(MIMEText(message, 'plain'))

#         # Add attachment if exists
#         if attachment and os.path.exists(attachment):
#             with open(attachment, "rb") as f:
#                 part = MIMEBase("application", "octet-stream")
#                 part.set_payload(f.read())
#                 encoders.encode_base64(part)
#                 part.add_header(
#                     "Content-Disposition",
#                     f"attachment; filename={os.path.basename(attachment)}"
#                 )
#                 msg.attach(part)

#         # Send email
#         with smtplib.SMTP(smtp_host, smtp_port) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.send_message(msg)
        
#         return True

#     except Exception as e:
#         flash(f"Email failed: {str(e)}", "danger")
#         return False

# def load_emails_from_csv():
#     emails = []
#     csv_file = "emails.csv"
    
#     try:
#         if os.path.exists(csv_file):
#             with open(csv_file, mode='r', encoding='utf-8') as f:
#                 reader = csv.DictReader(f)
#                 emails = [row for row in reader if all(row.get(k) for k in ['Name', 'Recipient', 'Subject'])]
#     except Exception as e:
#         flash(f"Error reading CSV: {str(e)}", "danger")
    
#     return emails

# def save_to_csv(data):
#     csv_file = "emails.csv"
#     fieldnames = ['Name', 'Recipient', 'Subject', 'Message', 'Attachment']
    
#     try:
#         with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             if f.tell() == 0:  # Write header if file is empty
#                 writer.writeheader()
#             writer.writerow(data)
#     except Exception as e:
#         flash(f"Error saving to CSV: {str(e)}", "danger")

# # Routes
# @app.route("/")
# def index():
#     return render_template("index.html", emails=load_emails_from_csv())

# @app.route("/send", methods=["POST"])
# def send_email_route():
#     # Get form data
#     form_data = {
#         'Name': request.form.get('name', '').strip(),
#         'Recipient': request.form.get('recipient', '').strip(),
#         'Subject': request.form.get('subject', '').strip(),
#         'Message': request.form.get('message', '').strip(),
#         'Attachment': ''
#     }

#     # Validate
#     if not all([form_data['Recipient'], form_data['Subject'], form_data['Message']]):
#         flash("Recipient, Subject and Message are required!", "danger")
#         return redirect(url_for('index'))

#     if not is_valid_email(form_data['Recipient']):
#         flash("Invalid email address!", "danger")
#         return redirect(url_for('index'))

#     # Handle file upload
#     if 'attachment' in request.files:
#         file = request.files['attachment']
#         if file.filename != '' and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(save_path)
#             form_data['Attachment'] = filename

#     # Send email and save to CSV
#     if send_email(
#         form_data['Name'],
#         form_data['Recipient'],
#         form_data['Subject'],
#         form_data['Message'],
#         os.path.join(app.config['UPLOAD_FOLDER'], form_data['Attachment']) if form_data['Attachment'] else None
#     ):
#         save_to_csv(form_data)
#         flash("Email sent successfully!", "success")
    
#     return redirect(url_for('index'))

# if __name__ == "__main__":
#     app.run(debug=True)


import os
import csv
import smtplib
import json
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER", "static/uploads")
app.secret_key = "supersecretkey"

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Function to send email
def send_email(name, recipient, subject, message, attachment=None):
    try:
        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASS")
         # Ensure required fields are not empty
        if not sender_email or not sender_password:
            flash("Email credentials are missing!", "danger")
            return

        if not recipient or not subject or not message:
            flash("Recipient, Subject, and Message are required!", "danger")
            return

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        msg.attach(MIMEText(message, 'plain'))

        # Attach file if exists
        if attachment:
            try:
                with open(attachment, "rb") as file:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment)}")
                    msg.attach(part)
            except Exception as e:
                flash(f"Attachment Error: {str(e)}", "warning")
        # Send email
        server = smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT")))
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        
        flash(f"Email sent successfully to {recipient}!", "success")

    except Exception as e:
        flash(f"Failed to send email: {str(e)}", "danger")

# Function to read emails from CSV
def load_csv_data():
    email_data = []
    csv_file = "emails.csv"
    
    if os.path.exists(csv_file):
        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                 if row and row["Name"] and row["Recipient"] and row["Subject"]:
                    email_data.append({
                        "name": row["Name"].strip(),
                        "recipient": row["Recipient"].strip(),
                        "subject": row["Subject"].strip(),
                        "message": row.get("Message", "").strip(),  # ✅ Extracting the message
                        "attachment": row.get("Attachment","").strip() 
                    })
                    
    
    return email_data 

@app.route("/", methods=["GET", "POST"])
def index():
    email_data = load_csv_data() 
    print("Email Data Loaded:", email_data)  # Debugging line

    return render_template("index.html", email_data=email_data or [])  # Ensure it's not None
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
@app.route("/send_email", methods=["POST"])
def send():
    name= request.form.get("name")
    recipient = request.form.get("recipient")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # Handle file upload
    attachment_path = None
    if "attachment" in request.files:
        file = request.files["attachment"]
        if file.filename != "":
            filename = secure_filename(file.filename)
            attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(attachment_path)

    return redirect(url_for("index"))
@app.route("/send_bulk_email", methods=["POST"])
def send_bulk_email():
    email_data = load_csv_data()

    if not email_data:
        flash("No email data found in CSV!", "danger")
        return redirect(url_for("index"))

    for entry in email_data:
        name = entry.get("name", "User")
        recipient = entry.get("recipient")
        subject = entry.get("subject")
        message = entry.get("message", "No message provided.")
        attachment = entry.get("attachment", "").strip()

        # Check if attachment exists
        attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], attachment) if attachment else None
        if attachment and not os.path.exists(attachment_path):
            attachment_path = None  # Ignore missing attachments

        send_email(name, recipient, subject, message, attachment_path)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
