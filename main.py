#! /usr/bin/python
# -*- coding:utf8 -*-


from datetime import datetime
import re
from bson.objectid import ObjectId
from bs4 import BeautifulSoup as bs4

from flask import Flask, \
    abort, request, flash, session, redirect

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
    _pg = 1
    posts = mdb.blog.find({})\
        .sort([('upload_time', -1),]).limit(config.PAGE_LEN)\
        .skip((_pg - 1) * config.PAGE_LEN)
    return {'posts': posts}


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


@app.route('/post/<post_id>', endpoint='post')
@util.blog_wrapper(pat='post.pat')
def post(post_id):
    '''
        post
    '''
    _post = mdb.blog.find_one({'_id': ObjectId(post_id)})
    return {'post': _post}


@app.route('/newpost', endpoint='newpost')
@util.blog_wrapper(pat='newpost.pat', login_required=True)
def newpost():
    '''
        newpost
    '''
    ret = {}
    return ret


@app.route('/do_newpost', endpoint='do_newpost', methods=['POST'])
@util.blog_wrapper(pat='', login_required=True)
def do_newpost():
    '''
        upload new posts
    '''
    title = request.form.get('title')
    article = request.form.get('article')

    _bdom = bs4(article)
    summary = re.sub('[\r\n ]+', ' ', \
        _bdom.get_text())
    summary = u'%s...' % summary[:40]

    blog_id = mdb.blog.insert({
        'title': title,
        'article': article,
        'summary': summary,
        'upload_time': datetime.now(),
        'author': session['owner'],
    })

    return redirect('/post/%s' % blog_id)


@app.route('/about', endpoint='about')
@util.blog_wrapper(pat='about.pat')
def about():
    '''
        about
    '''
    ret = {}
    return ret
