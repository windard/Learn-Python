# coding=utf-8

import os
from flask import Flask, request, session, escape
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': os.urandom(40),
    "REDIS_URL": "redis://127.0.0.1:6379/0"
})

redis_store = FlaskRedis(app)

form = """
        <form method="POST" action>
            <input type='test' name='name' >
            <input type='password' name='password'>
            <input type='submit' name='submit' value='登陆'>
        </form>
        """


@app.route('/')
def index():
    return "This is the index paga"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return form
    else:
        if redis_store.exists(request.remote_addr) and not int(redis_store.get(request.remote_addr)) < 5:
            return 'Login Failed overtimes , please try again later'
        if request.form.get('name') == 'windard' and request.form.get('password') == 'password':
            session['login'] = True
            session['username'] = 'windard'
            return 'Hello %s, Welcome back' % session['username']
        else:
            if redis_store.exists(request.remote_addr):
                redis_store.incr(request.remote_addr)
            else:
                redis_store.incr(request.remote_addr)
                redis_store.expire(request.remote_addr, 10 * 60)
            return 'Login Failed <br>' + form


if __name__ == '__main__':
    app.run(port=5067, host='0.0.0.0')
