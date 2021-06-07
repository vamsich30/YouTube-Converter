from pytube import YouTube
from direc_choose import location
from change_to_mp3 import file_check
from check_file_in_direc import file_in_direc
import os

try:
    yt = YouTube(input("Enter the URL : "))
except:
    print("ERROR please check your:\n  -Connection\n  -Please make sure pytube is installed"
          "\n  -URL must be a YouTube url\nPlease try again.")
    exit()

print("Press 1.Audio    2.Video    3.Audio + Video\nEnter your option : ",end=" ")
num = int(input())
if num <= 0 or num > 3:
    print(">o< Wrong input please try again >o<")
    exit()

if num == 1:
    t = yt.streams.filter(only_audio=True).first()
    print("File Size : "+str(round(t.filesize/(1024*1024))) + "MB")
    print("\..Please wait while it is Downloading../")
    print("Downloading....",t.title)
    out_file = t.download(output_path=location())
    base , ext = os.path.splitext(out_file)
    file_check(base,out_file,ext = ".mp3")

if num == 2:
    t = yt.streams.filter(only_video=True)
    print("File Size : "+str(round(t[0].filesize/(1024*1024))) + "MB")
    print("\..Please wait while it is Downloading../")
    print("Downloading....",t[0].title)
    out_file = t[0].download(output_path=location())
    base,ext = os.path.splitext(out_file)
    file_in_direc(base,out_file)

if num == 3:
    t = yt.streams.first()
    print("File Size : "+str(round(t.filesize/(1024*1024))) + "MB")
    print("\..Please wait while it is Downloading../")
    print("Downloading....",t.title)
    out_file = t.download(output_path=location())
    base,ext = os.path.splitext(out_file)
    file_in_direc(base,out_file)


# sample link : https://youtu.be/eVuPhZl4ksY
