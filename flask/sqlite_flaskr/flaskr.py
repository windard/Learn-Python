# coding=utf-8
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from datetime import timedelta

app = Flask(__name__)
app.config.from_pyfile('config.py')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, content from entries order by id desc')
    entries = [dict(title=row[0], content=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        # abort(401)
        flash("Please Login First",'error')
        return redirect(url_for('show_entries'))
    g.db.execute('insert into entries (title, content) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
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
