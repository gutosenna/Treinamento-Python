from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text='Bárbara Silva Medeiros, vamos assistir um filme?',
    lang=language
)

sp.save(audio)
playsound(audio)
