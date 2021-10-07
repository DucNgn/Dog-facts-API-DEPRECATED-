import flask
from flask_cors import CORS
from random import randrange
import json

from config import PORT

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["DEBUG"] = True

with open("data.json") as json_file:
    data = json.load(json_file)
    dataLength = len(data)

@app.route('/')
def home():
    return '''<h1>Welcome to Dog Facts API</h1> <a href="https://dukengn.github.io/Dog-facts-API" target="blank">Documentation</a>'''


@app.route('/api/v1/resources/dogs/all', methods=['GET'])
def api_all():
    print('Database length: ', len(data))
    return flask.jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Error 404:</1><p>The resource could not be found. Please check your query</p>", 404


@app.route('/api/v1/resources/dogs', methods=['GET'])
def api_number():
    results = []
    if 'number' in flask.request.args:
        number = int(flask.request.args['number'])
        for _ in range(number):
            results.append(data[randrange(dataLength)])
    elif 'index' in flask.request.args:
        requestIndex = int(flask.request.args['index'])
        if requestIndex >= 0 and requestIndex < dataLength:
            results.append(data[requestIndex])
    else:
        return page_not_found(404)
        
    return flask.jsonify(results)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
