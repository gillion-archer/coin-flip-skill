from mycroft import MycroftSkill, intent_file_handler
from random import randint

class CoinFlip(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

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

