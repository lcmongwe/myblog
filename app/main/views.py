from unicodedata import category
from flask import render_template,request,redirect,url_for,abort,flash

from app.main.forms import BLogForm, CommentForm
from . import main

# from ..models import  Pitch, User,Comment,Upvote,Downvote
# from .forms import PitchForm, CommentForm, UpvoteForm
# from flask_login import login_required,current_user
from .. import db
from flask.views import View,MethodView
# import markdown2


@main.route('/')

def index():
    form=CommentForm()
    
    return render_template('home.html', form=form)


@main.route('/profile')
def profile():
    
    return render_template("profile/profile.html")


@main.route('/write')
def write():
    form=BLogForm()
    
    return render_template("writer/writer.html",blog_form=form)

@main.route('/blogs')
def blogs():
    form=CommentForm()
    
    return render_template("allblogs.html",comment_form=form)

@main.route('/comment')
def comment():
    form=CommentForm()
    
    return render_template("comments.html",comment_form=form)