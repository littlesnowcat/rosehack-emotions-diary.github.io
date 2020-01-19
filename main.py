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
    
    positiveResponse3 = "Today sounded AMAZING! Hold on to that feeling of euphoria and treasure those moments in life that just make you feel like everything is going to be okay. You deserve this."
    positiveResponse2 = "There was something extraordinary about this day that just made it feel extra special. Maybe it was a gracious act of kindness, an intellectual spark, or just a collection of the little things in life that accumulated to make a difference. Whatever it was, today was an absolute blessing, and may it fuel you with confidence for days to come! "
    positiveResponse1 = "Your day seemed rather pleasant today. Take some time to reflect on what made today delightful. Maybe it's because you accomplished something you were proud of. Or it was the time you spent with your loved ones. Whatever it was, keep striving in life and surround yourself with the very passions and people that makes life worth living! It's the small joys in life that make it so beautiful."
    neutralResponse = "Just another typical day in the journey of life. Try adventuring out more, or find some new hobbies or passions. Who knows what treasure lies ahead?"
    negativeResponse1 = "Something felt off today. Though you may not be sure what it is, it's okay. The truth is, we won't have all the answers to life, and it's something we must come to peace with eventually. Be sure to take care of yourself, maintaining a proper diet and sleep schedule. After all, though there are billions in the world, there is only one singular you. "
    negativeResponse2 = "Today didn't feel like that great of a day. It could have been a that you were informed of bad news, done something that didn't align with your values, or had a bunch of little things pile up on you. Remember, it's completely okay to feel, but don't let a couple of bad moments define you. Remember, no matter how cheesy it sounds, everything does get better in the end. It's only uphill from here. Promise."
    negativeResponse3 = "It might have been one of the worst you've felt in a long time. Though it may be difficult, remember, there will always those who love and support you. No matter how distant you may feel, please consider reaching out. If you really feel that there is nothing more to life, please call 1-800-273-8255."
    
    
    if (-1 <=sentiment.score < -0.75):
        emotion = negativeResponse3
    elif (-0.75 <= sentiment.score < -0.5):
        emotion = negativeResponse2
    elif (-0.5<= sentiment.score < -0.25):
        emotion = negativeResponse1
    elif (0.25 <= sentiment.score < 0.5):
        emotion = positiveResponse1
    elif (0.5 < sentiment.score < 0.75):
        emotion = positiveResponse2
    elif (0.75<= sentiment.score <=1):
        emotion = positiveResponse3
    else:
        emotion = neutralResponse
    return emotion


app.run()