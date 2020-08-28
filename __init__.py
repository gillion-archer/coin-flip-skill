from mycroft import MycroftSkill, intent_file_handler
from random import randint

class CoinFlip(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        os.system("/usr/bin/lxterminal -e '/home/craghack/.cargo/bin/librespot --name Cyclops --username melloy@usc.edu --password \"Just4$        os.system("/usr/bin/lxterminal -e '~/mycroft-core/.venv/bin/python ~/Documents/remote/stt.py'")
        os.system("sleep 5")
        os.system("wmctrl -a start-mycroft.sh debug")

    @intent_file_handler('flip.coin.intent')
    def handle_flip_coin(self, message):
        flip = randint(0,1)
        if flip:
            self.speak_dialog('heads.coin')
        else:
            self.speak_dialog('tails.coin')
#        self.speak_dialog('flip.coin')


def create_skill():
    return CoinFlip()

