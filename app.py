import flask
from flask import request, jsonify
from random import randrange
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open("data.json") as json_file:
    data = json.load(json_file)
    dataLength = len(data)

@app.route('/')
def home():
    return '''<h1>Welcome to Dog Facts API</h1>'''


@app.route('/api/v1/resources/dogs/all', methods=['GET'])
def api_all():
    print('Database length: ', len(data))
    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Error 404:</1><p>The resource could not be found. Please check your query</p>", 404

@app.route('/api/v1/resources/dogs', methods=['GET'])
def api_number():
    results = []
    if 'number' in request.args:
        number = int(request.args['number'])
        for i in range(number):
            results.append(data[randrange(dataLength)])
    elif 'index' in request.args:
        requestIndex = int(request.args['index'])
        if requestIndex >= 0 and requestIndex < dataLength:
            results.append(data[requestIndex])
    else:
        return page_not_found(404)
        
    return jsonify(results)

if __name__ == '__main__':
    app.run()
