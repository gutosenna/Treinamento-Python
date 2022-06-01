# import webbrowser
# webbrowser.open("ex21.mp3")

# from pydub import AudioSegment
# from pydub.playback import play
# song = AudioSegment.from_mp3("ex21.mp3")
# print('playing sound using  pydub')
# play(song)

# from playsound import playsound
# playsound('/path/ex21.mp3')
# print('playing sound using  playsound')

# import vlc
# p = vlc.MediaPlayer("ex21.mp3")
# p.play()

# from pydub import AudioSegment
# from pydub.playback import play
# #
# song = AudioSegment.from_mp3("sound.wav")
# play(song)

# import os, time
# '''r = caminho absoluto'''
# os.startfile(r'C:\Users\GUTO SENNA\PycharmProjects\pythonProject\ex21.mp3')
# '''time=tempo e  sleep=dormir parar a execução'''
# time.sleep(10)

# from playsound import playsound
# print('Tocando: ')
# playsound('ex21.mp3')

import playsound
playsound.playsound('ex21.mp3')
#
# import pygame
# pygame.mixer.init()
# pygame.init()
# pygame.mixer_music.load('ex21.mp3')
# pygame.mixer_music.play()
# input()
# pygame.event.wait()

# import pygame
# import os
# pygame.init()
# if os.path.exists('ex21.mp3'):
#   pygame.mixer_music.load('ex21.mp3')
#   pygame.mixer_music.play()
#   pygame.mixer_music.set_volume(1)
#
#   clock = pygame.time.Clock()
#   clock.tick(10)
#
#   while pygame.mixer_music.get_busy():
#      pygame.event.poll()
#      clock.tick(10)
# else:
#   print('O arquivo musica.mp3 não está no diretório do script Python')

# import winsound
# winsound.PlaySound('ex21.wav', winsound.SND_FILENAME)

# import pygame
# pygame.mixer.init()
# pygame.mixer.music.load('ex21.mp3')
# pygame.mixer.music.play()
# input()
# pygame.event.wait()

# import pygame
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load('ex21.mp3')
# pygame.mixer.music.play()
# input() # <-Essa linha não tinha na explicação
# pygame.event.wait()

# import pygame
#
# pygame.mixer.init()
# pygame.mixer.music.load('ex21.mp3')
# pygame.mixer.music.play()
# input()

# from pygame import mixer
# mixer.init()
# mixer.music.load('ex21.mp3')
# mixer.music.play()
# input('Agora você escuta?')


# import pygame
# pygame.init()
# pygame.mixer.music.load('ex21.mp3')
# pygame.mixer.music.play()
# input('Nome da musica, pra parar de tocar só apertar ENTER')  # Essa linha vai segurar o programa funcionando para a musica tocar

# import pygame
#
# pygame.init()
# pygame.mixer_music.load('ex21.mp3')
# pygame.mixer_music.play()
# pygame.event.wait()
# input()

# import pygame
# pygame.mixer.init()
# pygame.mixer.music.load("ex21.mp3")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pass
