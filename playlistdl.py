from pytube import Playlist, YouTube
import os

url = ""
root_path = "D:\FUN\MUSIC\EasyTube"

def youtube(url):
    yt = YouTube(url)
    if not os.path.exists(f"{root_path}"):
        os.makedirs(f"{root_path}")
    os.chdir(f"{root_path}")
    print(f"Downloading {yt.title}")
    try:
        audio = yt.streams.filter(only_audio=True).first()
        file = audio.download()
        file_name, ext = os.path.splitext(file)
        new_name = file_name + ".mp3"
        os.rename(file, new_name)
        print("Done")
    except Exception:
        print(f"Something went wrong downloading {yt.title}")

def playlist(url):
    p = Playlist(url)
    c = len(p)
    if not os.path.exists(f"{root_path}\{p.title}"):
        os.makedirs(f"{root_path}\{p.title}")
    os.chdir(f"{root_path}\{p.title}")
    print(f"Downloading {p.title}")
    for video in p.videos:
        print(f"{c} remaining")
        try:
            audio = video.streams.filter(only_audio=True).first()
            file = audio.download()
            file_name, ext = os.path.splitext(file)
            new_name = file_name + ".mp3"
            os.rename(file, new_name)
            print(f"{video.title} downloaded")
        except Exception:
            print(f"Something went wrong downloading {video.title}")
        c -= 1
    print("Done")

while not "youtube.com" in url:
    url = input("Enter URL:")

if "playlist" in url:
    playlist(url)
elif "watch" in url:
    youtube(url)