from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=ZWopmb4du0I&list=RDCLAK5uy_k5faEHND0iXJljeASESqJ3A8UtRr2FL00&start_radio=1&rv=6EGg0_l-edc&ab_channel=LuanSantana'])