import os
from pathlib import Path

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

from flask_migrate import Migrate, MigrateCommand


from forms import LivechatForm
from text_model import TextAnalyser



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

        result = Result(message=message,gender=gender,cl=cl,pos=pos, neg=neg)

        db.session.add(result)
        db.session.commit()

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
