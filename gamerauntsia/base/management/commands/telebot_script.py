from django.core.management.base import BaseCommand
from django_simple_forum.models import Category
import telebot
import time
import re

TOKEN = '107547414:AAEXaH2tSNcnaehNq_7NNbNKb1VfDbaa6Qs'

COMMANDS = (
    ('kaixo', 'Kaixo mundua!'),
    ('foroa', 'Foroko aurkibidea ikusteko'),
    ('laguntza', 'Laguntzeko prest naukazu!'),
)


def start_telebot():

    tb = telebot.TeleBot(TOKEN)

    @tb.message_handler(func=lambda message: '#' in message.text)
    def command_hashtag(message):
        hashtags = ", ".join(re.findall(r"(?i)\#\w+", message.text))
        tb.send_message(message.chat.id, "Fororako gai hauek aipatu dituzu: "+hashtags)

    @tb.message_handler(commands=['kaixo', 'foroa', 'laguntza'])
    def command_list(message):
        if 'kaixo' in message.text:
            tb.send_message(message.chat.id, "Kaixo %s!" % (message.from_user.first_name))
        elif 'foroa' in message.text:
            if not '-k' or '-f' or '-t' in message.text:
                msg = 'Kategoriak:'
                categories = "\n".join(f.title for f in Category.objects.all().order_by('title'))
                msg += categories
                
            tb.send_message(message.chat.id, msg)
        else:
            cmd_lst = ''
            for cmd in COMMANDS:
                cmd_lst += "/%s - %s\n" % (cmd[0],cmd[1])
            tb.send_message(message.chat.id, "Komando zerrenda:\n"+cmd_lst)

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
