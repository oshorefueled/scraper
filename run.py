from flask import Flask
from app.api import summaryapi
from app.api import collapseapi
app = Flask(__name__)
app.register_blueprint(summaryapi.summary_api)
app.register_blueprint(collapseapi.collapse_api)

app.config["JSON_SORT_KEYS"] = False

@app.route("/")
def index():
    return "Hi, I scrape data"

if __name__ == '__main__':
    app.run(debug=True)