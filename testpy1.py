import pafy
from bs4 import BeautifulSoup
from  more_itertools import unique_everseen
import urllib.request
import re
import pickle


import sys
import codecs
if sys.stdout.encoding != 'utf8':
  sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'utf8':
  sys.stderr = codecs.getwriter('utf8')(sys.stderr.buffer, 'strict')



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
lis=[]
import os
path=u"C:/Users/Suhas/Dropbox/Public/Music/Songs"
filenames = next(os.walk(path))[2]
for t in filenames:
    lis.append((t.split('.',1)[0]))

for link in l:
    url2="https://www.youtube.com/" + (link.get('href'))
    video=pafy.new(url2)
    t=video.title
    if t not in Videolist:
        Videolist.append(t)
        if t not in lis:
            print (t)
            try:
                best=video.getbestaudio()
                filename=best.download(filepath="C:/Users/Suhas/Dropbox/Public/Music/Songs",quiet=False)
                print("Download Complete")
            except IOError:
                print("Error")
pickle.dump(Videolist, open( "save.p", "wb" ) )