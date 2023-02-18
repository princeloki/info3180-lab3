from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])
    subject = StringField('Subject', validators=[InputRequired(), Length(max=120)])
    message = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Submit')
