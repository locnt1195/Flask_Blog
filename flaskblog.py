from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/home")
def hello():
    return "Home Page"


@app.route("/aboutus")
def hello():
    return "About US""


if __name__ == '__main__':
    app.run(debug=True)
