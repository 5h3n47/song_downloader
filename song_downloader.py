
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import youtube_dl
import urllib.request

i=0
lis = []
textToSearch = input(str("Search for a song:  "))
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    #print('https://www.youtube.com' + vid['href'])
    temp = 'https://www.youtube.com' + vid['href']
    lis.append(temp)
#print(lis[0])
link = lis[0]  

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
