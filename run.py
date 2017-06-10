from flask import Flask
from app.api import summaryapi
app = Flask(__name__)
app.register_blueprint(summaryapi.summary_api)


@app.route("/")
def index():
    return "Hi, I scrape data"

if __name__ == '__main__':
    app.run(debug=True)