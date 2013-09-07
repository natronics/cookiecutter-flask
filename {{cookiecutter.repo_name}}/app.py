from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    site_defs = {'title': "{{project_name}}"}
    return render_template('index.html', **site_defs)

if __name__ == "__main__":
    app.debug = True
    app.run()
