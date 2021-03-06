#!/usr/bin/env python3

import json
import os
import subprocess
import time
import urllib.request
from pathlib import Path

__author__ = 'lqs'
__version__ = 0.3
__page__ = 'https://github.com/withlqs/BingWallpaper'


def set_wallpaper(file):
    # SCRIPT = """gsettings set org.gnome.desktop.background picture-uri file://%s"""
    # macOS version
    SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""
    subprocess.Popen(SCRIPT%file, shell=True)


def main():
    today = time.strftime("%Y%m%d")
    local_file = 'bingwallpaper'+today+'.jpg'
    local_path = str(Path.home()) + '/Pictures/'
    file = local_path+local_file
    if os.path.isfile(file):
        exit()
    url_base = 'http://cn.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1'
    codec = 'utf-8'
    print(local_path+local_file)
    webpage = urllib.request.urlopen(url_base)
    js = webpage.read().decode(codec)
    download_url = 'http://cn.bing.com' + json.loads(js)['images'][0]['url'].replace('1080', '1200')
    # download_url = 'http://cn.bing.com'+json.loads(js)['images'][0]['url']
    print(download_url)
    urllib.request.urlretrieve(download_url, file)
    set_wallpaper(file)


if __name__ == '__main__':
    main()

