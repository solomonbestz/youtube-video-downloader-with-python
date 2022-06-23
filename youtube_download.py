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
    
    def select_path(self):
        self.path = filedialog.askdirectory()
        self.path_field.delete(0, END)
        self.path_field.insert(END, self.path)

    def download(self):
        #get user path
        self.get_link = self.link_field.get()
        
        #get selected path
        self.user_path = self.path_field.get()

        #Download Video
        self.mp4_video = YouTube(self.get_link).streams.get_highest_resolution().download()
        self.video_clip = VideoFileClip(self.mp4_video)
        self.video_clip.close()

        #move the download file to selected directory
        shutil.move(self.mp4_video, self.user_path)
        self.title("Downloaded")

    def images(self):
        self.img = PhotoImage(file='media/yt.png')
        self.logo_img = self.img.subsample(2, 2)

    def labels(self):
        self.link_label = Label(text='Bestz Youtube Video Link', font=('Arial', 15))
        self.path_label = Label(text="Select Path For Download: ", font=('Arial', 10))

    def labels_insert(self):
        self.link_field.insert(END, "Paste Your Link Here.")
        self.path_field.insert(END, "Path To Save Downloaded Video.")

    def fields(self):
        self.link_field = Entry(borderwidth=0, highlightthickness=0)
        self.path_field = Entry(borderwidth=0, highlightthickness=0)

    def button(self):
        self.select_btn = Button(text='Select', command=self.select_path, border=0, background='red', height=2)
        self.download_btn = Button(text="Download", command=self.download, border=0, background='red', height=2)

    def canvas_pos(self):
        # Position for logo image
        self.canva.create_image(350, 60, image=self.logo_img) 
        # Position for fields
        self.canva.create_window(370, 280, width=250, height=30, window=self.path_field)
        self.canva.create_window(350, 220, width=350, height=30, window=self.link_field)
        # Position for labels
        self.canva.create_window(350, 170, window=self.link_label)
        self.canva.create_window(160, 280, window=self.path_label)
        # Postion for buttons
        self.canva.create_window(520, 280, window=self.select_btn)
        self.canva.create_window(350, 350, window=self.download_btn)

if __name__=='__main__':
    youtube = YTDownloader()
    youtube.images()
    youtube.labels()
    youtube.fields()
    youtube.labels_insert()
    youtube.button()
    youtube.canvas_pos()
    youtube.mainloop()


