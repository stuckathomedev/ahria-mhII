import pygame
from gtts import gTTS
import os
from pygame import mixer


dir_path = os.path.dirname(os.path.realpath(__file__))


def tts_set(message: str, language : str):
    tts = gTTS(text=message, lang=language)
    return tts


def tts_save(tts, file_name: str):
    tts.save(dir_path + "/" + file_name + ".mp3")


def tts_error():
    error_tts = tts_set("Sorry, an error has occured! Please try again!", 'en')
    tts_save(error_tts, 'error')

    mixer.init()
    mixer.music.load(dir_path + "\error.mp3")
    mixer.music.play()


def tts_play(file_name):
    while True:
        try:
            mixer.init()
            mixer.music.load(file_name)
            mixer.music.play()
        except pygame.error:
            tts_error()
            continue
        break
