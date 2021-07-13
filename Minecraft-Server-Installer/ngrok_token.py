import os, sys, replit

class TokenNotFound(Exception):
  pass

def refreshToken():
  token = os.getenv("ngrok_token", "Ngrok token doesn't exist!")
  os.system("./ngrok authtoken {token}".format(token=token))
