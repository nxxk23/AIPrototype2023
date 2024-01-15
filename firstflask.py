from flask import Flask, request, render_template, make_response 

import json

app = Flask(__name__) #start server

@app.route("/") #add route for search web
def helloworld():
    return "Hello, World!"

@app.route("/name") #add route for search web
def hellonink():
    return "Hello, Nink!"

@app.route("/home2") #add route for search web
def home2():
    return render_template("home.html",Name='nink')

if __name__=="__main__": 
    app.run(host='0.0.0.0', debug=True,port=5001) #host=0.0.0.0 :)
