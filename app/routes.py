#import sqlite3
from flask import Flask, render_template, flash, redirect, url_for
from app.forms import LoginForm
from app import app


#def get_db_conn():
#    conn = sqlite3.connect('flotilla.db')
#    conn.row_factory = sqlite3.Row
#    return conn


@app.route('/')
@app.route('/index')
def index():
    #conn = get_db_conn()
    #biz = conn.execute('select * from businesses').fetchall()
    #conn.close()
    biz = [
        {
            'user':{'username':'dancalla'},
            'business_name':'Pioneer',
            'industry':'Grocery',
            'address_city':'New York',
            'address_state':'NY'
        },
        {
            'user': {'username': 'ktshanny'},
            'business_name': 'Fairway',
            'industry': 'Grocery',
            'address_city': 'New York',
            'address_state': 'NY'
        },
        {
            'user': {'username': 'ktshanny'},
            'business_name': 'Paper Source',
            'industry': 'Crafts',
            'address_city': 'New York',
            'address_state': 'NY'
        }
    ]
    user = {'username': 'ktshanny'}
    return render_template('index.html', biz=biz, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
