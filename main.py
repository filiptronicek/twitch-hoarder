import os
import subprocess
import time
import sys


urls = ["https://www.twitch.tv/czechcloud", "https://www.twitch.tv/tubbo", "https://www.twitch.tv/marty_vole", "https://www.twitch.tv/cuky222"] 

if len(sys.argv) > 1:
    if sys.argv[1] == "stop":
        stop = True
    else:
        stop = False
else:
    stop = False

if not stop:
    for ind, url in enumerate(urls):
        print(url)
        os.system("tmux new-session -d -s yt-"+str(ind)+" 'youtube-dl " + url + " && exit'")

else:
    for i in range(len(urls)):
        os.system("tmux send-keys -t yt-"+str(i)+" C-c")