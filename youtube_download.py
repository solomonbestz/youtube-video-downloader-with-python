from app import *
from moviepy import * 
from moviepy.editor import VideoFileClip
from pytube import YouTube
from fonts import *
import shutil

class YTDownloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube Video Downloader")
        self.resizable(False, False)
        self.iconbitmap('media/favicon.ico')

    def canvass(self):
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
        self.header_text = Label(text="BESTZ YOUTUBE VIDEO DOWNLOADER", font=label_fonts(20, 'Helvetica'))
        self.link_label = Label(text='Input Video Link: ', font=label_fonts(10, 'Helvetica'))
        self.path_label = Label(text="Select Path For Download: ", font=label_fonts(10, 'Helvetica'))

    def labels_insert(self):
        self.link_field.insert(END, "Paste Your Link Here.")
        self.path_field.insert(END, "Path To Save Downloaded Video.")

    def fields(self):
        self.link_field = Entry(borderwidth=0, highlightthickness=0)
        self.path_field = Entry(borderwidth=0, highlightthickness=0)

    def button(self):
        self.select_btn = Button(text='Select', command=self.select_path, border=1, background='green', font= button_fonts(10, 'times'), height=1, width=10)
        self.download_btn = Button(text="Download", command=self.download, border=1, foreground = 'white', background='black', font= button_fonts(11, 'Helvetica'), height=2, width=30)

    def canvas_pos(self):
        # Position for logo image
        self.canva.create_image(350, 60, image=self.logo_img) 
        # Position for fields
        self.canva.create_window(400, 320, width=250, height=30, window=self.path_field)
        self.canva.create_window(400, 280, width=350, height=30, window=self.link_field)
        # Position for labels
        self.canva.create_window(170, 280, window=self.link_label)
        self.canva.create_window(190, 320, window=self.path_label)
        self.canva.create_window(380, 150, window=self.header_text)
        # Postion for buttons
        self.canva.create_window(570, 320, window=self.select_btn)
        self.canva.create_window(350, 370, window=self.download_btn)



