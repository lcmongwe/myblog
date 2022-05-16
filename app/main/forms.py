# from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class BlogForm(FlaskForm):
	title = StringField('Title', validators=[InputRequired()])
	description = TextAreaField("write your blog here",validators=[InputRequired()])
	submit = SubmitField('Submit')


class CommentForm(FlaskForm):
	description = TextAreaField('Add comment')
	submit = SubmitField()

