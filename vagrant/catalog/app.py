from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import make_response
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import json


app = Flask(__name__)
STATE_TOKEN_SIZE = 32
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web'][
    'client_id']


def generate_state_token():
    return ''.join([random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(STATE_TOKEN_SIZE)])


@app.route('/login')
def show_login():
    state = generate_state_token()
    session['state'] = state
    return render_template('login.html', page_title='Login', state=state)


@app.route('/gsignin', methods=['POST'])
def gsignin():
    if request.args.get('state') != session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    result = json.loads(request.data)


@app.route('/')
def hello():
    return render_template('home.html', page_title='Hello')


if __name__ == '__main__':
    app.secret_key = 'eA2TKYQyhcOY0MnqSuoy'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
