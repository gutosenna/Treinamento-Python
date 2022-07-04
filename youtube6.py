import youtube_dl
import os

os.chdir("C:\\Users\\GUTO SENNA\\OneDrive\\Música")
video_info = None
while True:
    videoORaudio = str(input('Deseja baixar em MP3 ou Video? [1] para MP3,  [2] para Vídeo, [3] Sair. -> '))
    if videoORaudio == '1':
        video_url = str(input("Coloque o link do vídeo abaixo: "))
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    elif videoORaudio == '2':
        with youtube_dl.YoutubeDL({}) as ydl:
            video_url = str(input("Coloque o link do vídeo abaixo: "))
            ydl.download([f'{video_url}'])
    elif videoORaudio == '3':
        print('Obrigado! Volte Sempre!...')
        break
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]

    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
