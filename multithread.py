from threading import Thread
import time
from pytube import Playlist, YouTube
import os

dl_dir = f"D:\Audio\EasyTube"

def youtube(url):
    yt = YouTube(url)
    if yt.check_availability() == None:
        if not os.path.exists(dl_dir):
            os.makedirs(dl_dir)
        os.chdir(dl_dir)
        title = yt.title.replace(".", "")
        if not os.path.exists(f"{dl_dir}\{title}.mp3"):
            try:
                audio = yt.streams.filter(only_audio=True).first()
                file = audio.download()
                file_name, ext = os.path.splitext(file)
                new_file_name = file_name + ".mp3"
                os.rename(file, new_file_name)
                print(f"Downloaded {title}")
            except Exception:
                print(f"Something went wrong ({title})")
                os.remove(file)
        else: print(f"{title}.mp3 already exists")
    else: print(f"Error")
        
url = input("Enter URL: ")

start_time = time.time()

if "watch" in url:
    youtube(url)
elif "playlist" in url:
    threads = []
    p = Playlist(url)
    dl_dir = f"D:\Audio\EasyTube\{p.title}"
    for i in range(len(p)):
        thread = Thread(target=youtube, args=(p[i],))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
print(f"Finished in {str(round(time.time() - start_time, 1))} seconds")