from threading import Thread
import time
from pytube import Playlist, YouTube
import os

dl_dir = "D:\Audio\EasyTube"
chars = '"\\/|:?*'

def youtube(url):
    yt = YouTube(url)
    title = yt.title
    for char in chars:
        if char in title:
            title = title.replace(char, "")
    title += ".mp3"
    if not os.path.exists(os.path.join(dl_dir, title)):
        try:
            audio = yt.streams.filter(only_audio=True).first()
            audio.download(filename=title)
            print(f"Downloaded {yt.title}")
        except Exception:
            pass
    else: print(f"{yt.title}.mp3 already exists")

url = input("Enter URL: ")

start_time = time.time()

if "watch" in url:
    if not os.path.exists(dl_dir):
        os.makedirs(dl_dir)

    os.chdir(dl_dir)
    youtube(url)

elif "playlist" in url:
    threads = []
    p = Playlist(url)
    dl_dir = os.path.join(dl_dir, p.title)
    if not os.path.exists(dl_dir):
        os.makedirs(dl_dir)
    os.chdir(dl_dir)

    for i in range(len(p)):
        thread = Thread(target=youtube, args=(p[i],))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
print(f"Finished in {str(round(time.time() - start_time, 1))} seconds")