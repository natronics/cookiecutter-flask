from flask import Flask, render_template
import config

app = Flask(__name__)

site_defs = config.site_defs


@app.route("/")
def hello():
    return render_template('index.html', **site_defs)

if __name__ == "__main__":
    app.debug = True
    app.run()
