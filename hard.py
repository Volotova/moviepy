import moviepy.editor
from pathlib import Path

video_path = Path("Nicki Minaj & Ice Spice – Barbie World (with Aqua)_mobclip.net.mp4")

video = moviepy.editor.VideoFileClip(f"{video_path}")
audio = video.audio
audio.write_audiofile(f"{video_path.stem}.mp3")