from unicodedata import category
from flask import render_template,request,redirect,url_for,abort,flash
from . import main

# from ..models import  Pitch, User,Comment,Upvote,Downvote
# from .forms import PitchForm, CommentForm, UpvoteForm
# from flask_login import login_required,current_user
# from .. import db
from flask.views import View,MethodView
# import markdown2




@main.route('/profile')
def profile():
    
    return render_template("profile/profile.html")



@main.route('/')

def index():
    
   
    return render_template('blogs.html')



