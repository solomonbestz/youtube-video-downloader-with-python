from tkinter import *
from tkinter import filedialog
from moviepy import * 
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil




# Default Variable Instantiation
screen = Tk()
title = screen.title('Youtube Downloader By Bestz Group')
canvas = Canvas(screen, width= 700, height=600)
canvas.pack()

#function to select file
def select_path(): 
    path = filedialog.askdirectory()
    path_field.delete(0, END)
    path_field.insert(END, path)

#function to download the video
def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_field.get()
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()

    #move the download file t selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Downloaded")

# App logo image
logo_img = PhotoImage(file='yt.png')

#resize
logo_img = logo_img.subsample(2, 2)

#link inpot field
link_field = Entry(screen, width=50)
link_field.insert(END, "Enter link here")
link_label = Label(screen, text='Bestz Youtube Video Link', font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download: ", font=('Arial', 10))
path_field = Entry(screen, width=50)
path_field.insert(END, "Path to save downloaded video here.")
select_btn = Button(screen, text='Select', command=select_path)

#Download buttons
download_btn = Button(screen, text="Download", command=download_file)

#Add logo image to the windows 
canvas.create_image(350, 60, image=logo_img)

#Add the widgets to windows
canvas.create_window(350, 170, window=link_label)
canvas.create_window(350, 220, window=link_field)

#Add the widgets to window path to download 
canvas.create_window(160, 280, window=path_label)
canvas.create_window(390, 280, window=path_field)
canvas.create_window(570, 280, window=select_btn)

#add the widget to window download button 
canvas.create_window(350, 350, window=download_btn)

if __name__=='__main__':
    screen.mainloop()

