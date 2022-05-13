from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class BLogForm(FlaskForm):
	title = StringField('Title')
	description = TextAreaField("write your blog")
	submit = SubmitField('Submit')


class CommentForm(FlaskForm):
	description = TextAreaField('Add comment')
	submit = SubmitField()

