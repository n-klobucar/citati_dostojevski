##from urllib.request import Request, urlopen

##req = Request(r'https://mudremisli.net/fjodor-mihajlovic-dostojevski-savest-citati-misli-izreke-poslovice/', headers={'User-Agent': 'Mozilla/5.0'})
##webpage = urlopen(req).read()
##print(webpage)

##import requests

##url = "https://mudremisli.net/fjodor-mihajlovic-dostojevski-savest-citati-misli-izreke-poslovice/"
##resp = requests.get(url)
##print (resp.status_code) # 200
##print (resp.content)

import random
with open("citati.txt", encoding="utf8") as f:
    fh=f.read().split("\n")
f.closed
fh_print = fh[random.randrange(0, len(fh)-1)]
print(fh_print)
with open("citati_web.html", "w", encoding="utf8") as f:
    f.write("<h1 style='margin-top: 20%;' align='center'>"+fh_print+"</h1>")
f.closed