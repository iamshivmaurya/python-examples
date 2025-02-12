# Required installations:
# pip install mysql-connector-python python-dotenv twilio

import smtplib
import mysql.connector
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration (store these in .env file)
MYSQL_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

EMAIL_CONFIG = {
    'address': os.getenv('EMAIL_ADDRESS'),
    'password': os.getenv('EMAIL_PASSWORD'),
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

TWILIO_CONFIG = {
    'account_sid': os.getenv('TWILIO_ACCOUNT_SID'),
    'auth_token': os.getenv('TWILIO_AUTH_TOKEN'),
    'from_number': os.getenv('TWILIO_PHONE_NUMBER')
}

def get_users_from_mysql():
    """Retrieve users from MySQL database"""
    try:
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT id, name, email, phone FROM users WHERE active = 1"
        cursor.execute(query)
        users = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return users
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return []

def send_email(receiver_email, subject, message):
    """Send email using SMTP"""
    try:
        with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
            server.ehlo()
            server.starttls()
            server.login(EMAIL_CONFIG['address'], EMAIL_CONFIG['password'])
            
            email_body = f"""\
From: {EMAIL_CONFIG['address']}
To: {receiver_email}
Subject: {subject}

{message}
"""
            server.sendmail(EMAIL_CONFIG['address'], receiver_email, email_body)
        print(f"Email sent to {receiver_email}")
        return True
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {str(e)}")
        return False

def send_sms(to_number, message):
    """Send SMS using Twilio"""
    try:
        client = Client(TWILIO_CONFIG['account_sid'], TWILIO_CONFIG['auth_token'])
        
        message = client.messages.create(
            body=message,
            from_=TWILIO_CONFIG['from_number'],
            to=to_number
        )
        print(f"SMS sent to {to_number} (ID: {message.sid})")
        return True
    except Exception as e:
        print(f"Failed to send SMS to {to_number}: {str(e)}")
        return False

def main():
    # Get users from database
    users = get_users_from_mysql()
    #print(users)
    #return
    
    if not users:
        print("No users found in database")
        return
    
    for user in users:
        # Send email
        email_subject = "Important Notification"
        email_message = f"Hello {user['name']},\nThis is an important message."
        send_email(user['email'], email_subject, email_message)
        
        # Send SMS
        sms_message = f"Hello {user['name']}, this is an important SMS notification."
        #send_sms(user['phone'], sms_message)

if __name__ == "__main__":
    main()