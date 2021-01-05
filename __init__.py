"""
LexiconCognito

Flask server module.
"""

from flask import Flask, render_template, redirect, request, url_for
from configparser import ConfigParser
from ast import literal_eval
from os import getcwd, urandom
from dbmanage import database

config = ConfigParser()
config.read("main.cfg")

dbmanage = database()

"""
if literal_eval(config["CORE"]["WAS_DATABASE_GENERATED"]) is False:
   dbmanage.generate()
   config["CORE"]["WAS_DATABASE_GENERATED"] = "True"
   with open("main.cfg", "wb") as config_dump:
      config.write(config_dump)
"""

app = Flask(__name__)
app.secret_key = urandom(4096)

@app.route("/")
def index():
    """
    Render index.html, to show repository index.
    :return: Index page.
    """
    return render_template("index.html", serverid = config["CORE"]["ID"])
    # TODO add page stats, page series for all items alphabetically

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
    :return: Tags page.
    """
    return render_template("tags.html", serverid = config["CORE"]["ID"])

@app.route("/profiles/")
def profiles():
    """
    Render profiles.html, to show publisher, source/distributor, and author entity management menu.
    :return: Profiles page.
    """
    return render_template("profiles.html", serverid = config["CORE"]["ID"])

@app.route("/settings/")
def settings():
    """
    Render settings.html, to show settings menu.
    :return: Settings page.
    """
    return render_template("settings.html", serverid = config["CORE"]["ID"])

@app.route("/content/")
def content():
    """
    Render content.html, to show repository content such as documents and media.
    :return: Contents page.
    """
    return render_template("content.html", serverid = config["CORE"]["ID"])

@app.route("/search/", methods = ["POST"])
def search():
    """
    Receive POST from client with search parameters.
    :return: redirects to searchresults.
    """
    if request.method == "POST": return redirect(url_for("search_results", search_type =  request.form["type"], search_term = request.form["term"], pagenumber = "1"))
    else:
        abort(405)

@app.route("/search/results/<search_type>/<search_term>/<int:pagenumber>/")
def search_results(search_type, search_term, pagenumber): # TODO parsing by date, tags, authors, publishers, and distributors
    """
    Render searchresults.html, to display content and run query from /search/.
    :param search_type: str, type of search
    :param search_term: str, term searched for
    :param pagenumber: str, result page to display, notated by number
    :return: searchresults page.
    """
    search_term = search_term.replace("+", " ").replace("%", " ")

    items = sorted(dbmanage.manage.cursor().execute("SELECT * FROM item").fetchall(), key = lambda x: x[1], reverse = True)

    for tuple_to_list_index in range(0, len(items)): items[tuple_to_list_index] = list(items[tuple_to_list_index])

    if " " in search_term: keywords = split(search_term)
    else: keywords = search_term

    lookup = {"id":0, "title":1, "authors":2, "date_added":3, "date_published":4, "notes":5, "publisher":6, "sourcedist":7, "tags":8, "path":9, "class":10, "aux":11}

    for items_index in range(0, len(items)):
        items[items_index].append(0)
        for keywords_index in range(0, len(keywords)):  # search method does not account for order of keywords
            if keywords[keywords_index].lower() in items[items_index][lookup[search_type]].lower(): items[items_index][12] += 1

        if len(keywords) == items[items_index][lookup[search_type]]: items[items_index][12] += 1
        if search_term.lower() in items[items_index][lookup[search_type]].lower(): items[items_index][12] += 1

    items = sorted(items, key = lambda x: x[12], reverse = True)

    if int(pagenumber) <= 0: pagenumber = "1"
    return render_template("searchresults.html", serverid = config["CORE"]["ID"], searchterm = search_term, searchtype = search_type, page = pagenumber, next = str(int(pagenumber) + 1), previous = str(int(pagenumber) - 1), items = items)

@app.route("/random/")
def random():
    """
    Load random content page.
    :return: Random content page.
    """

if __name__ == "__main__": app.run(debug = literal_eval(config["CORE"]["DEBUG"]), port = int(config["NET"]["PORT"]))
