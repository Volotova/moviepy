import moviepy.editor

video = moviepy.editor.VideoFileClip("Bumazhnyj_roman-7693_(anwap.org).mp4")
audio = video.audio
audio.write_audiofile("Bumazhnyj_roman_audio.mp3")