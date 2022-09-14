from mycroft import MycroftSkill, intent_file_handler


class MomMusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('music.mom.intent')
    def handle_music_mom(self, message):
        self.speak_dialog('music.mom')


def create_skill():
    return MomMusic()

