import requests, random, os
link = "https://your-repl-url.repl.co"
uri = link + "/changeip";
try:
  file = open("url.txt")
except:
  print("Error: url.txt not found")
ipadress = file.read()
file.close()
PARAMS = {'url': ipadress, 'apikey': os.getenv("apikeyforweb")}
requests.get(url = uri, params= PARAMS)
