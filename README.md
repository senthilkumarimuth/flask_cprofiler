# flask_cprofiler
Cprofiler for flask application. For each api request, it returns stats

# Sample output

![Alt text](./readme_files/sample.PNG?raw=true "vectorstore")

# Understandign the profiler output

ncalls: number of times the function was called.
tottime: total time spent inside the function (excluding calls to sub or inner functions).
percall: tottime divided by ncalls.
cumtime: total time spent inside the functions and any subfunctions called inside, including recursive calls.
percall: cumtime divided by ncalls.
filename:lineno(function): file name and line location for the respective entry.

# More details

https://codingshower.com/profiling-python-flask-web-apps-with-werkzeug-middleware-application-profiler/

