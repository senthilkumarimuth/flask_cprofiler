"""
C profiler for flask application

"""
import os
import shutil
from werkzeug.middleware.profiler import ProfilerMiddleware
from flask import Flask
from sub import add

# Setting up the app
app = Flask(__name__)
app.config['PROFILE'] = True
# configuring profiler
profile_path = './profile_reports'
if os.path.exists(profile_path):
    shutil.rmtree(profile_path)
os.mkdir(profile_path)
file = open('stats.txt', 'a')
app.wsgi_app = ProfilerMiddleware(app.wsgi_app,
                                  restrictions=("src",)
                                  )


@app.route("/", methods=["GET", "POST"])
def addition():
    c = add(100,100)
    return str(c)


if __name__ == "__main__":
    app.run(port=500, debug=True)
