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
   

@app.route('/isBetter', methods=['GET'])
def is_better():
    try:
        return "<h1>Fuck you, Buddy</h1>", 200, {'ContentType': 'text/hmtl'}
    except IOError:
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/sleep', methods=['GET'])
def get_sleep():
    try:
        os.system("sudo ssh -o StrictHostKeyChecking=no -i /home/ubuntu/.ssh/id_rsa -l drewmichel drews-mac-mini.lan \"./Scripts/sleep.sh\"")
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except IOError:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}


@app.route('/wake', methods=['GET'])
def get_wake():
    try:
        os.system("sudo ssh -o StrictHostKeyChecking=no -i /home/ubuntu/.ssh/id_rsa -l drewmichel drews-mac-mini.lan \"./Scripts/wake.sh\"")
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except IOError:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}


@app.route('/mute', methods=['GET'])
def get_mute():
    try:
        os.system("sudo ssh -o StrictHostKeyChecking=no -i /home/ubuntu/.ssh/id_rsa -l drewmichel drews-mac-mini.lan \"./Scripts/mute.sh\"")
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except IOError:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}


@app.route('/screensaver', methods=['GET'])
def get_screensaver():
    try:
        os.system("sudo ssh -o StrictHostKeyChecking=no -i /home/ubuntu/.ssh/id_rsa -l drewmichel drews-mac-mini.lan \"./Scripts/screensaver.sh\"")
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except IOError:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
