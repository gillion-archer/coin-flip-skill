from mycroft import MycroftSkill, intent_file_handler


class CoinFlip(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('flip.coin.intent')
    def handle_flip_coin(self, message):
        self.speak_dialog('flip.coin')


def create_skill():
    return CoinFlip()

