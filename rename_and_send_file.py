import os.path
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import main_env
from report_download import download_file
from main_env import *


FILES_DIR = os.path.dirname(__file__) + '\\files'


def rename_file():
    current_date = datetime.now().strftime("%d%m%Y")
    old_filename = "Daily.pdf"
    new_filename = f"{current_date}.pdf"
    old_filepath = os.path.join(FILES_DIR, old_filename)
    new_filepath = os.path.join(FILES_DIR, new_filename)
    try:
        os.rename(old_filepath, new_filepath)
        print(f"Файл успешно переименован в {new_filename}")
    except FileNotFoundError:
        print(f"Файл {old_filename} не найден в папке {FILES_DIR}")
    except Exception as e:
        print(f"Произошла ошибка при переименовании файла: {e}")
    return new_filename


def get_path(filename: str):
    # возвращает корректный путь до файла
    return os.path.join(FILES_DIR, filename)


download_file()

new_file_name = rename_file()

PDF_FILE = get_path(new_file_name)


# Параметры электронной почты
sender_email = main_env.sender_email
receiver_email = [main_env.receiver_email]
subject = main_env.subject

# Сообщение
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)  # receiver_email
message["Subject"] = subject

# Текст письма
body = ""
message.attach(MIMEText(body, "plain"))

# Вложение PDF
with open(PDF_FILE, "rb") as pdf_file:
    attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
    attachment.add_header("Content-Disposition", f"attachment; filename= {PDF_FILE[-12:]}")
    message.attach(attachment)

# Подключение к SMTP-серверу
smtp_server = main_env.smtp_server
smtp_port = main_env.smtp_port
smtp_username = main_env.smtp_username
smtp_password = main_env.smtp_password

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Письмо успешно отправлено!")

os.remove(PDF_FILE)
