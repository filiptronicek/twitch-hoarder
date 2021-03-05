import os
import subprocess
import time

urls = ["https://www.twitch.tv/czechcloud", "https://www.twitch.tv/tubbo", "https://www.twitch.tv/marty_vole"]
pids = []

for ind, url in enumerate(urls):
    print(url)
    os.system("tmux new-session -d -s yt-"+str(ind)+" 'youtube-dl " + url + " && exit'")

