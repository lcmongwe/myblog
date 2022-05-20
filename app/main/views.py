from unicodedata import category
from flask import render_template,request,redirect,url_for,abort,flash

from app.main.forms import BlogForm, CommentForm
from . import main

from ..models import *

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
@login_required
def write():
    form=BlogForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_blog = Blog(owner_id =current_user._get_current_object().id, description=description,title=title,category=category)
        db.session.add(new_blog)
        db.session.commit()

    '''
    View root page function that returns the index page and its data
    '''
    blog = Blog.query.filter_by().first()
    title = 'Home'
    general = Blog.query.filter_by(category="general")
    health = Blog.query.filter_by(category = "health")

    
    return render_template("writer/writer.html",blog=blog,blog_form=form,general=general,health=health)

@main.route('/blogs/new',methods = ['GET','POST'])
def blogs():
    user=current_user
    blogs=Blog.query.all()
    form=CommentForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_blog = Blog(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    return render_template("allblogs.html",comment_form=form,blogs=blogs)



@main.route('/comment/new/<int:blog_id>', methods = ['GET','POST'])
def comment(blog_id):
    form = CommentForm()
    blog=Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('main.comment', ))

    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    return render_template('comments.html', comment_form = form, comment = all_comments , blog=blog)


@main.route('/blog/<int:blog_id>/delete', methods=['GET','POST'])
@login_required
def delete_blog(blog_id):
  blog = Blog.query.get_or_404(blog_id)
  if blog.user != current_user:
    abort(403)
  db.session.delete(blog)
  db.session.commit()
  flash(f'Your post `Title: {blog.title}` has been Deleted!', 'info')
  return redirect(url_for('main.index'))