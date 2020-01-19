# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 02:38:21 2020

@author: myzae
"""


import os

from flask import Flask, render_template, request
app = Flask(__name__)

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\myzae\Documents\RoseHack Emotions Diary\RoseHack Emotions Diary\Sentiment Analysis-09adf8a39044.json"

# Instantiates a client
client = language.LanguageServiceClient()

@app.route("/", methods=['GET'])
def hello():
    return render_template("index.html")

@app.route("/sentiment")
def getSentiment():
    string = request.args.get("string")
    document = types.Document(
        content=string,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    emotion = "neutral";
    if (sentiment.score <= -0.2):
        emotion = "sad"
    if (sentiment.score >= 0.2):
        emotion = "happy"
    print (sentiment, emotion)
    return emotion

app.run()