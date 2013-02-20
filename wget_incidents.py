import os
f = open("incident_urls_complete.txt",'r')
urls = f.read().split('\n')
f.close()
os.chdir('incident_wget')
for url in urls:
    url = url.replace('%0D','').rstrip()
    print "getting: " + url
    os.system("wget --user-agent Mozilla/4.0 " + url + ' ')
