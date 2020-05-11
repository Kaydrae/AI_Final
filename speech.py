import os
from speech_recognition import Recognizer, Microphone, UnknownValueError


class speech():

    def myCommand(self):
        #listens for commands
        r = Recognizer()
        with Microphone() as source:
            print('Say something...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')
        # loop back to continue to listen for commands if unrecognizable speech is received
        except UnknownValueError:
            print('....')
            command = speech.myCommand(self)
        return command

    def AIResponse(audio):
        #speaks audio passed as argument
        print(audio)
        for line in audio.splitlines():
            os.system("say " + audio)
