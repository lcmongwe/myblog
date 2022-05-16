from unicodedata import category
from flask import render_template,request,redirect,url_for,abort,flash

from app.main.forms import BlogForm, CommentForm
from . import main

from ..models import *
# from .forms import PitchForm, CommentForm, UpvoteForm
from flask_login import login_required,current_user
from .. import db
from flask.views import View,MethodView
import requests,json
# import markdown2


@main.route('/' ,methods = ['GET','POST'])
def index():
    form=CommentForm()
    quotes=requests.get("http://quotes.stormconsultancy.co.uk/random.json")
    data=json.loads(quotes.content)
    
    return render_template('home.html', form=form,data=data)


@main.route('/profile',methods = ['GET','POST'])
@login_required
def profile():
    
    return render_template("profile/profile.html")


@main.route('/write',methods = ['GET','POST'])
def write():
    form=BlogForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        print(current_user._get_current_object().id)
        new_blog = Blog(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_blog)
        db.session.commit()

    '''
    View root page function that returns the index page and its data
    '''
    blog = Blog.query.filter_by().first()
    title = 'Home'
    return render_template("writer/writer.html",title=title,blog=blog,blog_form=form)

@main.route('/blogs',methods = ['GET','POST'])
def blogs():
    form=CommentForm()
  
    
    return render_template("allblogs.html",comment_form=form)

@main.route('/comment/new/<int:blog_id>', methods = ['GET','POST'])
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, blog_id = blog_id,blog=blog)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('main.comment', blog_id= blog_id))

    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    return render_template('comments.html', form = form, comment = all_comments )
