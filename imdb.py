import sys
import urllib2
import webbrowser as w
import re
import os
name=sys.argv[1]
name=os.path.basename(name)
name=name.replace(" ","%20")
url="http://www.omdbapi.com/?t="+name
r=urllib.urlopen(url)
web=r.read()
web=web.decode('UTF-8')

m=re.findall(r'tt[0-9]+',web)
url='http://www.imdb.com/title/'+m[0]+'/'
w.open_new_tab(url)
