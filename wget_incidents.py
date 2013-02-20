import os
f = open("incident_urls_complete.txt",'r')
urls = f.read().split('\n')
f.close()
os.chdir('incident_wget')
for url in urls:
    print "getting: " + url
    os.system("wget " + url)