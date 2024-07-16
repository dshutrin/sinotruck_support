import shutil
from zipfile import ZipFile
import os

from django.conf import settings

from .models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string


def fix_excel(excel_file):

    # Создаем временную папку
    tmp_folder = '/tmp/convert_wrong_excel/'
    os.makedirs(tmp_folder, exist_ok=True)

    # Распаковываем excel как zip в нашу временную папку
    with ZipFile(excel_file) as excel_container:
        excel_container.extractall(tmp_folder)

    # Переименовываем файл с неверным названием
    wrong_file_path = os.path.join(tmp_folder, 'xl', 'SharedStrings.xml')
    correct_file_path = os.path.join(tmp_folder, 'xl', 'sharedStrings.xml')
    os.rename(wrong_file_path, correct_file_path)

    # Запаковываем excel обратно в zip и переименовываем в исходный файл
    shutil.make_archive('yourfile', 'zip', tmp_folder)
    os.remove(excel_file)
    os.rename('yourfile.zip', excel_file)


def send_emails_to_managers(order):
    managers = CustomUser.objects.filter(role='MANAGER')
    managers = [x for x in managers if x.email and x.receive_emails]

    products = OrderItem.objects.filter(order=order)

    message_body = f"""Новый заказ от пользователя {order.user.username} ({order.user.email})\n\n№Заказа: {order.id}\n\nДетали заказа:\n"""
    sum_price = 0

    for product in products:
        sum_price += (product.count * product.product.price)
        message_body += f'\tСерийный номер: {product.product.serial_number}; Наименование: {product.product.name}; Марка: {product.product.mark}; Количество: {product.count}\n'

    message_body += f'\nОбщая стоимость: {sum_price}'
    html_message = render_to_string('mails/order_mail.html', {
        'products': products,
        'username': order.user.username,
        'order_id': order.id,
        'sum_price': sum_price
    })

    for manager in managers:
        send_mail(
            subject='Новый заказ на сайте SinotrukSupport',
            message=message_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[manager.email],
            html_message=html_message
        )
