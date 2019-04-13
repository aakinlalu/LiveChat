import os
from pathlib import Path

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import spacy
from spacy import displacy


class TextAnalyser:
    def __init__(self, text):
        self.text = text


    def opinion(self):
        blob = TextBlob(self.text, analyzer=NaiveBayesAnalyzer())
        classification = None
        positive = round(blob.sentiment.p_pos, 2)
        negative = round(blob.sentiment.p_neg, 2)
        if blob.sentiment.classification=="pos":
            classification="Positive"
        elif blob.sentiment.classification=="neg":
            classification="Negative"

        return classification, positive, negative

    def entity(self, filename):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)
        html_entity = displacy.render(doc, style="ent")
        output_path = Path(filename)
        output_path.open("w", encoding="utf-8").write(html_entity)


class LivechatForm(Form):
      Message = TextAreaField("Message")
      #Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
      Gender = SelectField('Gender', choices = [('Female', 'Female'),
      ('Male', 'Male')])
      submit = SubmitField("Submit")

app = Flask(__name__)
#app.secret_key = 'development key'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LivechatForm()

    if request.method == 'POST' and form.validate():
        message = form.Message.data
        gender = form.Gender.data
        Text_analyser = TextAnalyser(message)
        cl, pos, neg = Text_analyser.opinion()
        entity = Text_analyser.entity('templates/entity.html')


    else:
        message = None
        gender = None
        cl = None
        pos = None
        neg = None

    return render_template('index.html', form=form, message=message, gender=gender, cl=cl, pos=pos, neg=neg)


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__=='__main__':
    app.run()
