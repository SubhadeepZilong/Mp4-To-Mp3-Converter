import moviepy.editor 
from tkinter.filedialog import *



video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio=video.audio
save_path = asksaveasfilename()
audio.write_audiofile(save_path+".mp3")

# For video (with just audio) in mp4 format use the below format and comment the previous part

"""

video = askopenfilename()
video = moviepy.editor.AudioFileClip(video)
save_path = asksaveasfilename()
audio.write_audiofile(save_path+".mp3")

"""
