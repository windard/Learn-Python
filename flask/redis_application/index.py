# coding=utf-8

from flask import Flask, request
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.update({
    "REDIS_URL": "redis://127.0.0.1:6379/0"
})

redis_store = FlaskRedis(app)


@app.before_request
def before_request():
    setattr(request, 'view_times', redis_store.get(request.url))


@app.after_request
def after_request(f):
    redis_store.incr(request.url)
    return f


@app.route('/')
def index():
    return "This is the main paga , and it's your %s times view" % getattr(request, 'view_times')


@app.route('/page')
def page():
    return "I have seen you %s times" % getattr(request, 'view_times')


@app.route('/login')
def login():
    return "This is the %s times meet you ~" % getattr(request, 'view_times')

if __name__ == '__main__':
    app.run(port=5067, host='0.0.0.0')
