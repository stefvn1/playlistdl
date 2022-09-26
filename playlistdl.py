from pytube import Playlist, YouTube
import os
import time

def youtube(url):
    yt = YouTube(url)
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    os.chdir(root_path)
    title = yt.title.replace(".", "")
    if not os.path.exists(f"{root_path}\{title}.mp3"):
        print(f"Downloading: {title}")
        try:
            audio = yt.streams.filter(only_audio=True).first()
            file = audio.download()
            file_name, ext = os.path.splitext(file)
            new_name = file_name + ".mp3"
            os.rename(file, new_name)
            print("Done")
        except Exception:
            print(f"Something went wrong")
            os.remove(file)
    else: print(f"{title}.mp3 already exists")

def playlist(url):
    p = Playlist(url)
    c = len(p)
    if not os.path.exists(f"{root_path}\{p.title}"):
        os.makedirs(f"{root_path}\{p.title}")
    os.chdir(f"{root_path}\{p.title}")
    print(f"Downloading: {p.title}")
    for video in p.videos:
        title = video.title.replace(".", "")
        if not os.path.exists(f"{root_path}\{p.title}\{title}.mp3"):
            try:
                audio = video.streams.filter(only_audio=True).first()
                file = audio.download()
                file_name, ext = os.path.splitext(file)
                new_name = file_name + ".mp3"
                os.rename(file, new_name)
                print(f"{title} downloaded")
            except Exception:
                print(f"Something went wrong")
                os.remove(file)
        else: print(f"{title}.mp3 already exists")
        c -= 1

url = input("Enter URL: ")
root_path = "D:\Audio\EasyTube"

while not "youtube.com" in url:
    url = input("Enter URL: ")

start_time = time.time()

if "playlist" in url:
    playlist(url)
elif "watch" in url:
    youtube(url)

print(f"Finished in {str(round(time.time() - start_time, 1))} seconds")