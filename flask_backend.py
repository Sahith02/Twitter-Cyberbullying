from flask import Flask, redirect ,url_for, render_template

app=Flask(__name__)


a=[["Rude","You are a bad person"],["Not Rude","Hello , hi!"],["Rude","You suck"]]

l=5
@app.route("/",methods=["POST", "GET"])
def home():
	
    return render_template("Bullying.html",content=a)

    

if __name__=="__main__":
    app.run()
