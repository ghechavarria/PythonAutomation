#pip3 install pytube
import pytube  
import os

abspath = os.path.abspath(__file__)
currentDirectory = os.path.dirname(abspath)
os.chdir(currentDirectory)

try:
    video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'   
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.filter(res="720p").first()  
    video.download(currentDirectory)  
    print("Download Successfull !!")
except:
    print("Something Went Wrong !!")