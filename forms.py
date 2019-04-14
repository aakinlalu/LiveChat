from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError

class LivechatForm(Form):
      Message = TextAreaField("Message")
      #Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
      Gender = SelectField('Gender', choices = [('Female', 'Female'),
      ('Male', 'Male')])
      submit = SubmitField("Submit")
