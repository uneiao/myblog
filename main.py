#! /usr/bin/python
# -*- coding:utf-8 -*-


from flask import Flask, render_template, \
    abort, url_for, request, flash, session, redirect

from  model import mdb
import config
import util


app = Flask(__name__)
app.config.from_object('config')


@app.route('/', endpoint='index')
@util.blog_wrapper(pat='index.pat')
def index():
    '''
        index
    '''
    ret = {}
    return ret


@app.route('/xlogin', endpoint='login')
@util.blog_wrapper(pat='login.pat')
def login():
    '''
        login
    '''
    if session.get('is_logined'):
        flash('You were logged in')
        return redirect('/')
    return {}


@app.route('/do_login', endpoint='do_login', methods=['POST'])
@util.blog_wrapper()
def do_login():
    '''
        do_login
    '''
    email = request.form.get('email', None)
    password = request.form.get('password', None)

    owner = {}
    if email and password:
        password = util.md5_with_salt(password, config.SALT)
        owner = mdb.owner.find_one({'email': email, 'md5': password})
        print 'md5: %s' % password
    else:
        abort(404)

    if not owner:
        abort(404)

    session['is_logined'] = True
    session['owner'] = owner['name']
    return redirect('/')


@app.route('/logout', endpoint='logout')
@util.blog_wrapper(login_required=True)
def logout():
    '''
        logout
    '''
    session.pop('is_logined')
    session.pop('owner')
    return redirect('/')


@app.route('/newpost', endpoint='newpost')
@util.blog_wrapper(pat='index.pat', login_required=True)
def newpost():
    '''
        newpost
    '''
    ret = {}
    return ret
