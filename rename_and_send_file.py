import os.path
from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from report_download import download_file
from env_test import *


files_dir = os.path.dirname(__file__) + '\\files'


# Переименование файла с именем под текущую дату
def rename_file():
    current_date = datetime.now().strftime("%d%m%Y")
    old_filename = "Daily.pdf"
    new_filename = f"{current_date}.pdf"
    old_filepath = os.path.join(files_dir, old_filename)
    new_filepath = os.path.join(files_dir, new_filename)
    try:
        os.rename(old_filepath, new_filepath)
        print(f"Файл успешно переименован в {new_filename}")
    except FileNotFoundError:
        print(f"Файл {old_filename} не найден в папке {files_dir}")
    except Exception as e:
        print(f"Произошла ошибка при переименовании файла: {e}")
    return new_filename


# Возвращает корректный путь до файла
def get_path(filename: str):
    return os.path.join(files_dir, filename)


download_file(browser, files_dir, report_url, login, password)

new_file_name = rename_file()

PDF_FILE = get_path(new_file_name)


# Сообщение
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Текст письма
body = ""
message.attach(MIMEText(body, "plain"))

# Вложение PDF
with open(PDF_FILE, "rb") as pdf_file:
    attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
    attachment.add_header("Content-Disposition", f"attachment; filename= {PDF_FILE[-12:]}")
    message.attach(attachment)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Письмо успешно отправлено!")

os.remove(PDF_FILE)
