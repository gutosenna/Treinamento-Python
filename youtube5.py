import youtube_dl

with youtube_dl.YoutubeDL({}) as ydl:
    ydl.download([f'{video}'])