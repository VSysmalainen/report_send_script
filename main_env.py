import os


login = os.getenv('RZD_USER', default='login')
password = os.getenv('RZD_PASSWORD', default='password')
browser = os.getenv('BROWSER', default='Edge')
sender_email = os.getenv('SENDER_EMAIL', default='sender email')
receiver_email = os.getenv('RECEIVER_EMAIL', default='receiver email')
subject = os.getenv('SUBJECT', default='subject')
smtp_server = os.getenv('SMTP_SERVER', default='smtp server')
smtp_port = os.getenv('SMTP_PORT', default='port')
smtp_username = os.getenv('SMTP_USERNAME', default='smtp username')
smtp_password = os.getenv('SMTP_PASSWORD', default='smtp password')
