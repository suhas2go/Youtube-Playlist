import pafy
from bs4 import BeautifulSoup
from  more_itertools import unique_everseen
import urllib.request
import re
import pickle
try:
	Videolist = pickle.load( open( "save.p", "rb" ) )
except IOError:
	Videolist=[]
url='https://www.youtube.com/playlist?list=PLojXuFcACH_LmZkjpbA1cnnr3h_GZpDkk'
html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page,"html.parser")
def filterit(href):
    return href and re.compile("watch").search(href)
l=soup.findAll(href=filterit)

from os import listdir
from os.path import isfile, join
mypath="C:/Users/Suhas/Dropbox/Public/Music/Songs"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for link in l:
    url2="https://www.youtube.com/" + (link.get('href'))
    video=pafy.new(url2)
    t=video.title
    if t not in Videolist:
        Videolist.append(t)
        if t not in onlyfiles:
            print (t)
            best=video.getbestaudio()
            filename=best.download(filepath="C:/Users/Suhas/Dropbox/Public/Music/Songs",quiet=False)
pickle.dump(Videolist, open( "save.p", "wb" ) )