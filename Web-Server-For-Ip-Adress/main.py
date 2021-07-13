import os
from flask import Flask, request, render_template;
from replit import db

app = Flask(__name__, template_folder='template', static_folder='static')

app.config["DEBUG"] = True


APIKEY = os.getenv("apikeyforweb")

@app.route('/')
def index():
  try:
    ip = db["ip"]
  except:
    ip = "None"
  return render_template('index.html', ipadress=ip);


@app.route('/changeip', methods=["GET"])
def change():
  if(request.args.get("apikey") == APIKEY):
   db["ip"] = request.args.get("url");
   return "changed", 200;
  else:
    return "wrong api key", 401;

app.run(host="0.0.0.0")
