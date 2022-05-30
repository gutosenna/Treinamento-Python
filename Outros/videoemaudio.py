import moviepy.editor

video = moviepy.editor.VideoFileClip('videoplayback.mp4')
audio_data = video.audio
audio_data.write_audiofile('audio.mp3')
