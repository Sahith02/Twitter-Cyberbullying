from flask import Flask, redirect, url_for, render_template, request
import tweepy
import sys
app = Flask(__name__)
import cPickle as c
import os
from sklearn import *
from collections import Counter

app = Flask(__name__)

a = []

l = 5
info = ""
num_comments = 0


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        info = request.form["twitter_id"]
        num_comments = request.form["number_of_comments_id"]
        username = str(info)

        maxreplies = num_comments
        tweet_replies = []



        def tweetextraction(username, maxreplies):
            consumer_key = "nuVGJn0bEsYiKJ7mKAPTwkskK"
            consumer_secret = "XwrP0uU74FzgOE2p5X2EFkgLtrv4sXEvwOBl1FgmSR1gjOM5SX"
            access_token = "1284091258638462976-0aO8tuh7lhsWXtf6Jck2vV1twJzGE4"
            access_token_secret = "x7Ux4p4AwW7oZocVYhwTJZEYVlSUzo20EOW4WX4B1CyLw"
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            tweetwithreply = dict()
            i = 0
            for full_tweets in tweepy.Cursor(api.user_timeline, screen_name=username, timeout=999).items(1):
                tweet = full_tweets.text
            for replies in tweepy.Cursor(api.search, q='to:' + username, result_type='mixed', timeout=1500).items(100):
                if hasattr(replies, 'in_reply_to_status_id_str'):
                    if (replies.in_reply_to_status_id_str == full_tweets.id_str and i < maxreplies):
                        i += 1
                        tweet_replies.append(replies.text)
                        print(i)
            return tweet

        tweet = tweetextraction(username, maxreplies)

        def load(clf_file):
            with open(clf_file) as fp:
                clf = c.load(fp)
            return clf

        def make_dict():

            words = []
            Lines = []
            f = open('yaya.txt', 'r')
            Lines1 = f.readlines()
            for lo in Lines1:
                Lines.append(lo.lower())

            for line in Lines:
                yo = line.split(",")
                jo = yo[0]
                words += jo.split(" ")

            for i in range(len(words)):
                if not words[i].isalpha():
                    words[i] = ""

            dictionary = Counter(words)
            del dictionary[""]
            return dictionary.most_common(2000)

        clf = load("text-classifier.mdl")

        d = make_dict()

        u = ""
        jp = tweet_replies
        opi = 0
        for t in tweet_replies:

            features = []
            inp = []

            for xy in t:
                inp.append(xy.lower())
            if inp[0] == "exit":
                break
            for word in d:
                features.append(inp.count(word[0]))
            res = clf.predict([features])
            if res[0] >= 1:
                print('Rude')
                u = u + t + "\nRude\n"

                a.append(["Rude",t])

            else:
                u = u + t + "\nNot Rude\n"
                a.append(["Not Rude",t])


        return redirect(url_for("user", usr=a))
    else:
        return render_template("Bullying.html")


@app.route("/<usr>")
def user(usr):
    return render_template("classification.html", content=a)


if __name__ == "__main__":
    app.run(debug=True)
