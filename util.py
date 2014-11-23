#! /usr/bin/python
# -*- coding:utf-8 -*-


import md5
from flask import abort, session, render_template


def md5_with_salt(_str, salt):
    m = md5.new()
    m.update(_str)
    m.update(salt)
    return m.hexdigest()


def blog_wrapper(pat=None, login_required=False):
    def response_handler(f):
        def response_handled(*largs, **kwargs):
            if login_required and session.get('is_logined') is not True:
                abort(404)

            add_common = {}

            if session.get('is_logined'):
                add_common['owner'] = session.get('owner')

            res = f(*largs, **kwargs)

            response = res

            if isinstance(res, dict):
                res.update(add_common)
                response = render_template(pat, **res)

            return response

        return response_handled
    return response_handler
