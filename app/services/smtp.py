from __future__ import absolute_import

from typing import Any

import asyncio
import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .celery import celery_app
from ..api.operation.users import generate_code, save_code


async def send_message(*, id: int, email: str = ""):
    code = generate_code()
    save_code(id, code)

    message = MIMEMultipart("alternative")
    message['From'] = ""
    message['To'] = email
    message["Subject"] = "Please activate your username as soon as possible !"

    html_message = MIMEText(
        f"<html><body><a href='http://127.0.0.1:8000/users/activated/{id}?code={code}'>请点击本链接激活您的账户</a></body></html>",
        _subtype="html", _charset="utf-8"
    )

    message.attach(html_message)

    await aiosmtplib.send(message, hostname="smtp.163.com", port=25, username="", password="")


@celery_app.task(name="send_message_task")
def async_send_message(*, id: int, email: str = ""):
    asyncio.run(send_message(id=id, email=email))
