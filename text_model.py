import os
from pathlib import Path

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
