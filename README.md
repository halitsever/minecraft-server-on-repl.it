
<div align="center"> <img src="https://i.ibb.co/t8qFxnN/tenor.gif"> <h1>Minecraft Server on Repl.it</h1> <h2>Requirements for open minecraft server on repl.it:</h2> <ul> <li> A boosted repl </li> <li> Always on activated 2 repl (One of them web server the other one for minecraft server) </li> <li> Ngrok token (<a href="https://dashboard.ngrok.com/get-started/your-authtoken">From here</a> You can open an account and take) </li> <li> Dropbox <a href="https://www.dropbox.com/developers/apps/create"> Account and dropbox application key</a> </li> <li> <a href="https://www.spigotmc.org/resources/drivebackupv2.79519/">DrivebackupV2</a> extension (Spigot/PaperMC for) </li> </ul> <h3>Setup</h3> <p> First create two repls, we will use one for the web server and the other for the minecraft server. 
<h3>
<a href="https://replit.com/@halitsever/Minecraft-Server">Minecraft Server-fork this first</a><br>
<a href="https://replit.com/@halitsever/Web-Server-For-Minecraft-Server">Web Server for show ip adress-then fork it</a>
</h3>
From here <a href="https://www.dropbox.com/developers/apps/create"> Create dropbox application.</a> 

<a href="https://www.dropbox.com/developers/apps/create"> Take ngrok token from here.</a>

 Enter the following keys from hidden logins to your Minecraft server repl: <br>
 <img src="https://i.ibb.co/v3VjCTS/Screenshot-from-2021-07-13-16-10-44.png"><br>
 Dropbox_Token => <a href="https://www.dropbox.com/developers/apps/create"> From here</a> <br>
 The key you get for the application you created apikeyforweb => apikey for the request we will send to the web server (For example: Test#123456789) <br>
  ngrok_token => Online token via ngrok.com we're done here.

Now open getrequest.py and link = Replace the value of the variable "https://your-repl-url.repl.co" with the replin url you second open Here, our operations are completed, now it remains to prepare the webserver. 

Enter the repl you created for the web server, open the apikeyforweb key here in the secrets section and <quote> "apikeyforweb => apikey for the request we will send to the web server (For example: Test#123456789)" </quote> be the same as the key here. 

<img src="https://i.ibb.co/Vvtmbxq/Screenshot-from-2021-07-13-16-29-23.png"> 

The last thing we need to do after installation <a href="https://www.spigotmc.org/resources/drivebackupv2.79519/">DriveBackupV2 </a>plugin install. Download the jar file from here and upload it to server/plugins.<br> Then here <a href="https://github.com/halitsever/minecraft-server-on-repl.it/blob/main/Minecraft-Server-Installer/server/plugins/DriveBackupV2/config.yml">config file Replace the default config file. 
  </a><br>
If you typed Apikey correctly, the server will write on the site you typed into the getrequest.py.

</p> OK now! Login to the server <a style="color:green">/linkaccount </a> <a style="color:red">dropbox </a> sync your account by typing Create the first backup manually, type /drivebackup backup for it. Then every 15 minutes your plugins will save the world as long as you are on the server. </div>
