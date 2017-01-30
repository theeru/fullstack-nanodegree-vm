import json
import random
import string
from functools import wraps
from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for

from catalog.models.categories import Category
from catalog import session as db_session

app = Flask(__name__)
STATE_TOKEN_SIZE = 32
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web'][
    'client_id']


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def csrf(f):
    """
    Adds Cross-Site Request Forgery protection to a function
    """
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if request.method == 'GET':
            state = request.args.get('state')
        else:
            state = request.form.get('state')

        app.logger.info('STATE: %s' % state)

        if state != session['state']:
            response = make_response(json.dumps('Invalid state token'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        return f(*args, **kwargs)
    return decorated_func


def login_required(f):
    """
    Requires a logged in user for a function
    """
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if not session.get('user'):
            response = make_response(json.dumps('No authorized'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        return f(*args, **kwargs)
    return decorated_func


def generate_state_token():
    return ''.join([random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(STATE_TOKEN_SIZE)])


@app.route('/gsignin', methods=['POST'])
def gsignin():
    session['state'] = generate_state_token()
    session['user'] = request.form['email']
    return ''


@app.route('/logout', methods=['GET'])
@csrf
def logout():
    session.clear()
    return ''


@app.route('/')
def home():
    categories = Category.query.all()
    return render_template('home.html', page_title='Home',
                           categories=categories)


@app.route('/catalog/<category_name>/items')
def view_category(category_name):
    return category_name


@app.route('/catalog/categories/create', methods=['POST'])
@login_required
@csrf
def create_category():
    app.logger.info('Handling create category')
    category_name = request.form['category_name']
    app.logger.info('Category name: %s' % category_name)
    category = Category(name=category_name)
    db_session.add(category)
    db_session.commit()
    return redirect(url_for('view_category', category=category_name))


@app.route('/catalog/categories/form', methods=['GET'])
@login_required
def new_category_form():
    return render_template('new_category.html')


if __name__ == '__main__':
    app.secret_key = \
        '\xe9{\xd40\xd6\x1bjw(\xf0\x86\xae\xd48F\xa7\x0c\x01\xc3HQ\x10\xb8\xaf'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
