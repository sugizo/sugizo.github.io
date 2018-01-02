# -*- coding: utf-8 -*-

if request.function != 'user':
    auth.requires_login()(lambda: None)()

# user
def user(): 
    if 'login' in request.args:
        db.auth_user.username.label = T("Username or Email")
        auth.settings.login_userfield = 'username'
        if request.vars.username and not IS_EMAIL()(request.vars.username)[1]:
            auth.settings.login_userfield = 'email'
            request.vars.email = request.vars.username
            request.post_vars.email = request.vars.email
            request.vars.username = None
            request.post_vars.username = None
 
        return dict(form=auth()) 
    return dict(form=auth())

# download
@cache.action()
def download():
    return response.download(request, db)

# call
def call():
    session.forget()
    return service()

# error
def error():
    return dict()

# data
@auth.requires_signature()
def data():
    return dict(form=crud())

# index
def index():
    return locals()