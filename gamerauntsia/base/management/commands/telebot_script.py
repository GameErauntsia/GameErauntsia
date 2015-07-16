from django.core.management.base import BaseCommand
import telebot
import time

TOKEN = '107547414:AAEXaH2tSNcnaehNq_7NNbNKb1VfDbaa6Qs'

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            if 'Kaixo' in m.text:
                text = 'Kaixo!'
                tb.send_message(chatid, text)


def start_telebot():
    tb = telebot.TeleBot(TOKEN)
    tb.set_update_listener(listener) #register listener
    tb.polling()
    #Use none_stop flag let polling will not stop when get new message occur error.
    tb.polling(none_stop=True)
    # Interval setup. Sleep 3 secs between request new message.
    #tb.polling(interval=3)
    while True: # Don't let the main Thread end.
        pass

class Command(BaseCommand):
   help = 'Telebot'
   def handle(self, *args, **options):
       start_telebot()