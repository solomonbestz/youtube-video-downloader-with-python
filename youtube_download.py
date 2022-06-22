from tkinter import *
from tkinter import filedialog
from moviepy import * 
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil



class YTDownloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube Video Downloader")
        self.resizable(False, False)
        self.iconbitmap('media/favicon.ico')
        self.canva = Canvas(width= 700, height=600)
        self.canva.pack()
    
    def images(self):
        self.img = PhotoImage(file='media/yt.png')
        self.logo_img = self.img.subsample(2, 2)

    def canvas_pos(self):
        self.canva.create_image(350, 60, image=self.logo_img)

if __name__=='__main__':
    youtube = YTDownloader()
    youtube.images()
    youtube.canvas_pos()
    youtube.mainloop()


