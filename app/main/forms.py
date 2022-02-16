from unicodedata import category
import flask_simplemde
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField , SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us something about yourself", validators=[DataRequired()])
    submit = SubmitField('Submit')

class PitchesForm(FlaskForm):

    title = StringField('Pitch title', validators=[DataRequired()])
    category = SelectField("Category", choices =[(1,'Technology'),(2,'Fitness'),(3,'Interview'),(4,'Product pitch')],validators=[DataRequired()])
    content = TextAreaField('Write your pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')    

class CommentsForm(FlaskForm):
    comment = TextAreaField('Write your comment')
    submit = SubmitField('Submit')