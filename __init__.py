"""
LexiconCognito

Flask server module.
"""

from flask import Flask, render_template
from configparser import ConfigParser
from ast import literal_eval

config = ConfigParser()
config.read("main.cfg")

app = Flask(__name__)

@app.route("/")
def index():
   """
   Render index.html, to show repository index.
   :return: Index page.
   """
   return render_template("index.html", serverid = config["CORE"]["ID"])

@app.route("/upload/")
def upload():
   """
   Render upload.html, to show document upload menu.
   :return: Upload page.
   """
   return render_template("upload.html", serverid = config["CORE"]["ID"])

@app.route("/tags/")
def tags():
   """
   Render tags.html, to show tag management menu.
   :return:
   """

if __name__ == "__main__":
   app.run(debug = literal_eval(config["CORE"]["DEBUG"]), port = int(config["NET"]["PORT"]))
