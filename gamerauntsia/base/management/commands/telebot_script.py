from django.core.management.base import BaseCommand
from django_simple_forum.models import Category, Forum, Topic
from django.conf import settings
import telebot
import time
import re

COMMANDS = (
    ('kaixo', 'Kaixo mundua!'),
    ('foroa', 'Foroko aurkibidea ikusteko'),
    ('laguntza', 'Laguntzeko prest naukazu!'),
)


def start_telebot():

    tb = telebot.TeleBot(settings.TELEBOT_TOKEN)

    @tb.message_handler(func=lambda message: '#' in message.text)
    def command_hashtag(message):
        hashtags = ", ".join(re.findall(r"(?i)\#\w+", message.text))
        tb.send_message(message.chat.id, "Fororako gai hauek aipatu dituzu: "+hashtags)

    @tb.message_handler(commands=['kaixo', 'foroa', 'laguntza'])
    def command_list(message):
        text = message.text
        if 'kaixo' in text:
            tb.send_message(message.chat.id, "Kaixo %s!" % (message.from_user.first_name))
        elif 'foroa' in text:
            msg = 'Gaia zuzenean bilatzeko:\n /foroa -bilatu <bilaketa>\n\n'
            msg += 'Gaien traolak jakiteko:\n /foroa -k <kategoria> -f <foroa>\n\n'
            if '-bilatu' in text:
                msg = 'Bilaketa emaitza:\n'
                find = text[text.find('-bilatu')+8:].strip()
                if not len(find)<3:
                    topics = "\n".join('#GE'+str(t.id)+' - '+t.title for t in Topic.objects.filter(title__icontains=find).order_by('title'))
                    msg += topics or 'Ez da ezer aurkitu...'
                else:
                    msg = 'Mesedez, sartu 3 hizkitik gorako bilaketa!'
            elif not '-k' in text and not '-f' in text:
                msg += 'Kategoriak:\n'
                categories = "\n".join('#'+c.title.replace(' ','_') for c in Category.objects.all().order_by('title'))
                msg += categories or 'Ez da ezer aurkitu...'
            elif '-k' in text  and not '-f' in text:
                msg += 'Foroak:\n'
                cat = text[text.find('-k')+3:].replace('#','').replace('_',' ').strip()
                forums = "\n".join('#'+f.title.replace(' ','_') for f in Forum.objects.filter(category__title=cat).order_by('title'))
                msg += forums or 'Ez da ezer aurkitu...'
            elif '-f' in text:
                msg = 'Gaiak:\n'
                foru = text[text.find('-f')+3:].replace('#','').replace('_',' ').strip()
                topics = "\n".join('#GE'+str(t.id)+' - '+t.title for t in Topic.objects.filter(forums__title=foru).order_by('title'))
                msg += topics or 'Ez da ezer aurkitu...'
            else:
                msg = 'Komando okerra! Saiatu berriz...'
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
    while true: # Don't let the main Thread end.
        pass

class Command(BaseCommand):
   help = 'Telebot'
   def handle(self, *args, **options):
       start_telebot()
