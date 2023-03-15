# flask_cprofiler
Cprofiler for flask application. For each api request, it returns stats

# Sample output

![Alt text](./readme_files/sample.PNG?raw=true "vectorstore")

# warning

When a restriction is applied, stream to file feature is not working!

# Understandign the profiler output

ncalls: number of times the function was called.<br />
tottime: total time spent inside the function (excluding calls to sub or inner functions).<br />
percall: tottime divided by ncalls.<br />
cumtime: total time spent inside the functions and any subfunctions called inside, including recursive calls.<br />
percall: cumtime divided by ncalls.<br />
filename:lineno(function): file name and line location for the respective entry.<br />

# More details

https://codingshower.com/profiling-python-flask-web-apps-with-werkzeug-middleware-application-profiler/

