import sys
import urllib.request
import json
import subprocess
import getpass
import time
__author__ = 'lqs'

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

today = time.strftime("%Y%m%d")
local_file = 'bingwallpaper'+today+'.jpg'
local_path = '/Users/' + getpass.getuser() + '/Pictures/'
file = local_path+local_file
url_base = 'http://cn.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1'
codec = 'utf-8'
print(local_path+local_file)

def set_wallpaper(file):
    subprocess.Popen(SCRIPT%file, shell=True)

webpage = urllib.request.urlopen(url_base)
js = webpage.read().decode(codec)
download_url = json.loads(js)['images'][0]['url']
print(download_url)
urllib.request.urlretrieve(download_url, file)

set_wallpaper(file)
