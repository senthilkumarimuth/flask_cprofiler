"""
flask application

"""

from flask import Flask
from sub import add

# Setting up the app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def addition():
    c = add(100,100)
    return str(c)


if __name__ == "__main__":
    app.run(port=500, debug=True)
