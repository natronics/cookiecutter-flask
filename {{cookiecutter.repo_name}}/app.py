from flask import Flask, render_template
from util import *
import config

app = Flask(__name__)

site_defs = config.site_defs


@app.route("/")
def hello():
    return render_template('index.html', **site_defs)


@app.route("/data.json")
@json
def data():
    return {'obj': "object"}, 200

if __name__ == "__main__":
    app.debug = True
    app.run()
