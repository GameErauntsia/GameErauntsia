from django.core.management.base import BaseCommand
from django_simple_forum.models import Category, Forum, Topic, Post
from gamerauntsia.gamer.models import GamerUser
from django.conf import settings
import telebot
import time
import re
from daemon_command import DaemonCommand

COMMANDS = (
    ('kaixo', 'Kaixo mundua!'),
    ('kodea', 'Zure Game Erauntsiko profilarekin lotzeko kodea'),
    ('foroa', 'Foroko aurkibidea ikusteko'),
    ('laguntza', 'Laguntzeko prest naukazu!'),
)

def start_telebot():

    tb = telebot.TeleBot(settings.TELEBOT_TOKEN)

    @tb.message_handler(func=lambda message: '#' in message.text)
    def command_hashtag(message):
        hashtag = re.findall(r"(?i)\#\w+", message.text)[0]
        try:
            topic_id = int(hashtag.replace("#GE",""))
            topic = Topic.objects.get(id=topic_id)
            text = message.text.replace(hashtag,"").replace("@ge_bot","").strip()

            if message.from_user.id and GamerUser.objects.filter(telegram_id=message.from_user.id).exists():
                user = GamerUser.objects.get(telegram_id=message.from_user.id)
                post_title = topic.title
                if topic.last_post():
                    post_title = 'Re: ' + topic.last_post().title.replace('Re: ','')

                post = Post()
                post.topic = topic
                post.title = post_title
                post.body = text
                post.creator = user
                post.telegram_id = str(message.from_user.id)
                post.save()

                tb.send_message(message.chat.id, u"Aupa %s! Mezua jasota \U0001F44D" % (message.from_user.first_name))
            else:
                tb.send_message(message.chat.id, u"Barkatu... nor zara? \U0001F605\nKonfiguratu zure Telegram /kodea eta saiatu berriz!")

        except:
            tb.send_message(message.chat.id, u"Barkatu %s, ez dut zure mezua ulertu \U0001F62D" % (message.from_user.first_name))

    @tb.message_handler(commands=['kaixo', 'foroa', 'kodea', 'laguntza'])
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
        elif 'kodea' in text:
            if message.chat.id < 0:
                tb.send_message(message.chat.id, "Mesedez %s, eskatu zure kodea niri zuzenean. Ez erabili taldeak horretarako" % (message.from_user.first_name))
            else:
                tb.send_message(message.chat.id, "Zure kodea: %d\n\nGorde zenbaki hau zure Game Erauntsiko profilean" % (message.from_user.id))
        else:
            cmd_lst = ''
            for cmd in COMMANDS:
                cmd_lst += "/%s - %s\n" % (cmd[0],cmd[1])
            tb.send_message(message.chat.id, "Komando zerrenda:\n"+cmd_lst)

    #Use none_stop flag let polling will not stop when get new message occur error.
    tb.polling()
    # Interval setup. Sleep 3 secs between request new message.
    #tb.polling(interval=3)

class Command(DaemonCommand):

    STDOUT = '../log/telebot.err'
    STDERR = STDOUT
    
    def loop_callback(self):
        start_telebot()
        time.sleep(2.5)        
