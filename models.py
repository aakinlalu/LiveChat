from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.types import Text
from sqlalchemy import Integer, String, TIMESTAMP


from datetime import datetime




class Result(db.Model):
    __tablename__ = 'results'


    id =db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    text=db.Column(db.String())
    gender=db.Column(db.String())
    sentiment=db.Column(db.String())
    p_pos=db.Column(db.Integer)
    p_neg=db.Column(db.Integer)
    #result_all = db.Column(JSON(astext_type=None, none_as_null=False))

    def __init__(self, text, gender, sentiment, p_pos, p_neg):
        self.text = text
        self.gender = gender
        self.sentiment = sentiment
        self.p_pos=p_pos
        self.p_neg=p_neg
        #self.result_all=result_all


    def __repr__(self):
        return '<id {}>'.format(self.id)
