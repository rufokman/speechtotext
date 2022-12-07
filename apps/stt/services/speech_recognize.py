import speech_recognition as sr

from schedule import Scheduler
import schedule


def speech_recognition(source):
    r = sr.Recognizer()
    # source = "C:/Users/admin/Downloads/111.wav"
    audio_ex = sr.AudioFile(source)
    with audio_ex as source:
        audiodata = r.record(audio_ex)
    text = r.recognize_google(audio_data=audiodata, language='RU')
    return text
