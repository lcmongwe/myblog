from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class BLogForm(FlaskForm):
	title = StringField('Title', validators=[InputRequired()])
	description = TextAreaField("write your blog",validators=[InputRequired()])
	category = SelectField('select category', choices=[ ('memes','memes'), ('thought','thought'),('religious','religious'),('motivational','motivational')],validators=[InputRequired()])
	submit = SubmitField('Submit')


class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField()

