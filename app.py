from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")


@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    return render_template("index.html", mars_data=mars_data)

# Scrape Data and pull into Mongo DBp
@app.route('/scrape')
def web_scrape():
    mars = mongo.db.mars
    mars_data = scrape.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run()

