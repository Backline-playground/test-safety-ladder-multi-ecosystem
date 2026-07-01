from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def index():
    return "ok"


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("file")
    if f is None:
        return "no file", 400
    name = secure_filename(f.filename)
    return f"received {name}"


if __name__ == "__main__":
    app.run()
