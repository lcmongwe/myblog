# from email.policy import default
from enum import unique
from unicodedata import category
from . import db
from flask_login import UserMixin,current_user
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'{self.username}'


class Blog(db.Model):
    '''
    '''
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment',backref='blog',lazy='dynamic')
    
    
    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.order_by(pitch_id=id).desc().all()
        return blogs
