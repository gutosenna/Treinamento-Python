from pytube import Playlist, YouTube

playlist = Playlist("https://www.youtube.com/watch?v=ZWopmb4du0I&list=RDCLAK5uy_k5faEHND0iXJljeASESqJ3A8UtRr2FL00&start_radio=1&rv=14C28JSO-sg&ab_channel=LuanSantana")

for video in playlist:
    youtube = YouTube(video)

    youtube.streams.get_highest_resolution().download()