from django.core.management.base import BaseCommand
from django.conf import settings

import telebot

from daemon_command import DaemonCommand


def start_telebot():
    tb = telebot.TeleBot(settings.PYSSTELEBOT_TOKEN)

    @tb.message_handler(
        commands=[
            "hello",
        ]
    )
    def command_list(message):
        text = message.text
        if "hello" in text:
            tb.send_message(
                message.chat.id, "Hello %s!" % (message.from_user.first_name)
            )

    tb.polling()


class Command(DaemonCommand):
    STDOUT = "../log/telebot.err"
    STDERR = STDOUT

    def loop_callback(self):
        start_telebot()
        time.sleep(2.5)
