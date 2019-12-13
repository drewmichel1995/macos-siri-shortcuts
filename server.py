from flask import Flask, abort, redirect, url_for, render_template, request
from flask_cors import CORS, cross_origin
import json
import os

rootDir = '../output/'
app = Flask(__name__, template_folder=rootDir)
CORS(app)


@app.route('/')
def root():
    return render_template('index.json')
   

@app.route('/sleep', methods=['GET'])
def get_sleep():
    try:
        os.system("osascript -e 'tell application \"Finder\" to sleep'")
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except IOError:
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6969)
