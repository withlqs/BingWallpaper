
import sys
import urllib.request
import json
import subprocess
import getpass
__author__ = 'lqs'

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_wallpaper(file):
    subprocess.Popen(SCRIPT%file, shell=True)

webpage = urllib.request.urlopen('http://cn.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1')
js = webpage.read().decode("utf-8")
download_url = json.loads(js)['images'][0]['url']

local_path = '/Users/' + getpass.getuser() + '/Pictures/bingwallpaper.jpg'
urllib.request.urlretrieve(download_url, local_path)

set_wallpaper(local_path)
