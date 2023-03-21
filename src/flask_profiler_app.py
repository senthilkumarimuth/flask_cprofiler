"""
profiler for flask application

"""
import os
import shutil
from werkzeug.middleware.profiler import ProfilerMiddleware
from app import app
app.config['PROFILE'] = True
# configuring profiler
profile_path = '../reports/profile/profs'
if os.path.exists(profile_path):
    shutil.rmtree(profile_path)
os.mkdir(profile_path)
file = open('../reports/profile/stats.txt', 'w')
app.wsgi_app = ProfilerMiddleware(app.wsgi_app,stream= file, profile_dir=profile_path)

if __name__ == "__main__":
    app.run(port=500, debug=True)