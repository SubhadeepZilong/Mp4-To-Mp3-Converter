import moviepy.editor 
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio=video.audio
save_path = asksaveasfilename()
audio.write_audiofile(save_path+".mp3")