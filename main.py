import sys
from urllib.request import urlopen
import json
__author__ = 'lqs'

webpage = urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1')
js = webpage.read().decode("utf-8")
location = json.loads(js)['images'][0]['url']

print(location)
