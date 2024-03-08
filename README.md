# report_send_script
Скрипт при помощи selenium генерирует отчёт для клиента на Jaspersoft, скачивает его в формате PDF, переименовывает в соответствии с текущей датой и отправляет по почте.
Указать через ENV переменные параметры входа и отправки.
Пример:
RZD_USER;
RZD_PASSWORD;
BROWSER;
MAIN_URL;
SECOND_URL;
SENDER_EMAIL;
RECEIVER_EMAIL;
SUBJECT;
SMTP_SERVER;
SMTP_PORT;
SMTP_USERNAME;
SMTP_PASSWORD.

Запуск локально:
1) создать виртуальное окружение
2) в корне проекта выполнить команду pip install -r -requirements.txt для установки зависимостей
3) выполнить команду python rename_and_send_file.py
4) дождаться окончания выполнения скрипта
