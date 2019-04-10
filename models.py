from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.types import Text
from sqlalchemy import Integer, String, TIMESTAMP


from datetime import datetime




class Result(db.Model):
    __tablename__ = 'results'


    id =db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    message=db.Column(db.String(500))
    gender=db.Column(db.String(15))
    cl=db.Column(db.String(15))
    pos=db.Column(db.Float)
    neg=db.Column(db.Float)
    #result_all = db.Column(JSON(astext_type=None, none_as_null=False))

    def __init__(self, message, gender, cls, pos, neg):
        self.message = message
        self.gender = gender
        self.cl= cl
        self.pos=p_pos
        self.ganeg=p_neg
        #self.result_all=result_all


    def __repr__(self):
        return '<id {}>'.format(self.id)
