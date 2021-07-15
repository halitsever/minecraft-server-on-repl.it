import os, json, time, ngrok_token, zipfile

SERVER_VERSION = "1.16.5"
ngrok_region = "eu"
javaArgs = "-Xms2048M -Xmx2048M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true" 

# You can adjust the ram size by changing the -Xms<ram_mb>M -Xmx<ram_mb>M lines. I also recommend looking here: https://aikar.co/2018/07/02/tuning-the-jvm-g1gc-garbage-collector-flags-for-minecraft/ If you don't have a hacker plan, change it to 200mb but remember that lag will be too much.


installed = True
def write(filename,content):
  f = open(filename,"a")
  f.write("")
  f.close()
  f = open(filename,"w")
  f.write(str(content))
  f.close()

if os.path.exists('./server/plugins/DriveBackupV2/DropboxCredential.json'):
  try:
    import dropbox
  except:
    os.system("pip install dropbox")
    import dropbox

  dbx = dropbox.Dropbox(os.getenv('Dropbox_Token'))


def downloadFromDropbox(filename, dropboxpath):
  with open(filename, "wb") as f:
    metadata, res = dbx.files_download(dropboxpath)
    f.write(res.content)
    with zipfile.ZipFile(filename,"r") as zipextract:
      zipextract.extractall("./server")

def downloadMap():
  if (installed == True):
    if os.path.exists('./server/plugins/DriveBackupV2/DropboxCredential.json'):
      os.system("rm -rf ./world.zip ./plugins.zip")
      os.system("rm -rf ./server/plugins ./server/world")
      os.system("rm -rf ./server/logs") # I added this line to save more space. You can delete it if you want.
      mapfilepath = dbx.files_list_folder('/Apps/DriveBackup/backups/world/').entries[0].path_lower
      pluginsfilepath = dbx.files_list_folder('/Apps/DriveBackup/backups/plugins/').entries[0].path_lower
      downloadFromDropbox("world.zip", mapfilepath)
      downloadFromDropbox("plugins.zip", pluginsfilepath)
      print("Plugins downloaded from dropbox")
      os.system("rm -rf ./world.zip ./plugins.zip")
      print("Downloanded zips extracted and deleted")


def downloadPaperMC():
  os.system("wget -O server.jar 'https://papermc.io/api/v1/paper/" + SERVER_VERSION + "/latest/download'")
  os.system("install-pkg openjdk-8-jre-headless")
  os.system("mkdir server")
  os.system("cp server.jar server/server.jar")

def downloadNgrok():
  os.system("wget -O ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip")
  with zipfile.ZipFile("ngrok.zip", "r") as zipextract: 
    zipextract.extractall("./");
    os.system("rm -rf ngrok.zip")



def runServer():
  if os.path.exists("./server.jar"):
    print("Server.jar running...")
  else:
    downloadPaperMC()
  downloadMap()
  if os.path.exists("./ngrok"):
    print("Ngrok running...")
  else:
    downloadNgrok()
  os.system("chmod 777 ./ngrok")
  os.system("./ngrok tcp --region=" + ngrok_region +" 25565 >/dev/null &")
  time.sleep(10)
  os.system("curl http://localhost:4040/api/tunnels > tunnels.json")
  with open('tunnels.json') as data_file:
    try:
      datajson = json.load(data_file)
    except:
      print("")
  time.sleep(10)
  os.system("echo {url} > url.txt".format(url=datajson['tunnels'][-1]["public_url"].replace("tcp://","")))
  os.system("python3 getrequest.py >/dev/null &") # This line is for the webserver. See the getrequest.py file to understand the code.
  os.chdir("server")
  write("eula.txt","eula=true")
  os.system("java {javaArgs} -jar server.jar -nogui".format(javaArgs=javaArgs))


try:
  f = open("server-is-installed")
  f.close
except:
  installed = False

ngrok_token.refreshToken()

if installed == False:
  os.system("rm -rf server server.jar")
  write("server-is-installed","If this file is here, the server is installed. If you want to reinstall the server, then delete this file.")
  runServer()
else:
  runServer()
