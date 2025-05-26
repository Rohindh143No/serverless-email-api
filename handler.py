import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(event, context):
    try:
        print("\n--- Incoming Request ---")
        print("Raw event:", event)
        
        body = json.loads(event['body'])
        print("Parsed JSON body:", body)

        receiver_email = body.get('receiver_email')
        subject = body.get('subject')
        body_text = body.get('body_text')

        if not receiver_email or not subject or not body_text:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields."})
            }
            print("--- Response ---")
            print("StatusCode       :", response["statusCode"])
            print("Body             :", response["body"])
            return response

        # Your sender Gmail
        sender_email = os.environ.get('SENDER_EMAIL')
        sender_password = os.environ.get('SENDER_PASSWORD')

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body_text, 'plain'))

        # Gmail SMTP configuration
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully!"})
        }
        print("--- Response ---")
        print("StatusCode       :", response["statusCode"])
        print("Body             :", response["body"])
        return response

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
        print("--- Response (Exception) ---")
        print("StatusCode       :", response["statusCode"])
        print("Body             :", response["body"])
        return response
