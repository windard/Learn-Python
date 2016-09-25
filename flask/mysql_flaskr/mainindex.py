# coding=utf-8

import os
import string
import random
import StringIO
import Image, ImageDraw, ImageFont, ImageFilter

from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from contextlib import closing
from datetime import timedelta

from flask_sqlalchemy import SQLAlchemy

from flask_wtf import Form
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User %r>"%self.username


@app.after_request
def shutdown_session(response):
    db.session.remove()
    return response

@app.route('/')
def show_entries():
    users = User.query.all()
    entries = [dict(title=row.username, content=row.password)  for row in users]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        flash("Please Login First",'error')
        return redirect(url_for('show_entries'))
    user = User('%s'%request.form['title'],'%s'%request.form['text'])

    db.session.add(user)
    db.session.commit()
    flash('New entry was successfully posted','flash')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = "username"
            flash('You were logged in','flash')
            return redirect(url_for('show_entries'))
        flash(error,'error')
    return render_template('login.html')
    # return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out','flash')
    return redirect(url_for('show_entries'))

@app.route('/api')
def query():
    params = request.args
    return "You Are %s Query For %s"%(params.get('name',None),params.get('for',None))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(threaded=True,port=8888)
    app.secret_key = app.config['SECRET_KEY']
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
