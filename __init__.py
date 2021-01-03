"""
LexiconCognito

Flask server module.
"""

from flask import Flask, render_template
from configparser import ConfigParser
from ast import literal_eval
from os import getcwd
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

@app.route("/search/")
def search():
    """
    Receive POST from client with search parameters.
    :return: redirects to searchresults.
    """
    if request.method == "POST": return redirect(url_for("search/results/" + request.form["type"] + "/" + request.form["term"] + "/" + "1"))
    else: abort(405)

@app.route("/search/results/<search_type>/<search_term>/<int:pagenumber>/")
def search_results(search_type, search_term, pagenumber):
    """
    Render searchresults.html, to display content and run query from /search/.
    :param search_type: str, type of search
    :param search_term: str, term searched for
    :param pagenumber: str, result page to display, notated by number
    :return: searchresults page.
    """
    raw = dbmanage.manage.cursor().execute("SELECT " + request.form["type"] + " FROM item").fetchall()
    items = []

    for raw_index in raw: items.append(raw[raw_index][0])
    items.sort()

    if request.form["type"] == "tags" or request.form["type"] == "authors":
        raise NotImplementedError  # TODO special search for tags and authors, with lookups for numeric IDs
    elif request.form["type"] == "publisher" or request.form["type"] == "distributor":
        raise NotImplementedError  # TODO lookups for publishers and distributors, with numeric IDs
    else:
        keywords = split(request.form["term"])
        parsed = {}
        for items_index in range(0, len(items)):
            parsed[items[items_index]] = 0
            for keywords_index in range(0, len(keywords)):  # search method does not account for order of keywords
                if keywords[keywords_index].lower() in items[items_index].lower(): parsed[items[items_index]] += 1

            if len(keywords) == parsed[items[items_index]]: parsed[items[items_index]] += 1

        results = sorted(parsed.items(), key = lambda x: x[1], reverse = True)

        fill = dbmanage.manage.cursor().execute("SELECT * FROM item").fetchall()

        for convert_index in range(0, len(results)):
            del results[reduce_index][1]
            results[reduce_index][1] =

    if int(pagenumber) <= 0: pagenumber = "1"
    return render_template("searchresults.html", serverid = config["CORE"]["ID"], searchterm = search_term, searchtype = search_type, page = pagenumber, next = str(int(pagenumber) + 1), previous = str(int(pagenumber) - 1))

@app.route("/random/")
def random():
    """
    Load random content page.
    :return: Random content page.
    """

if __name__ == "__main__": app.run(debug = literal_eval(config["CORE"]["DEBUG"]), port = int(config["NET"]["PORT"]))
