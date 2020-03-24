from flask import Flask
from flask_caching import Cache
from datetime import datetime

app = Flask(__name__)

cache=Cache(app,config={'CACHE_TYPE': 'simple'})

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/without_cached')
def without_cached():
    return str(datetime.utcnow())


@app.route('/with_cached')
@cache.cached(timeout=5)
def with_cached():
    return str(datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)
