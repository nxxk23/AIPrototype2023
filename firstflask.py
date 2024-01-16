from flask import Flask, request, render_template, make_response 

import json

app = Flask(__name__) #start server

@app.route("/") #add route for search web1
def helloworld():
    return "Hello, World!"

@app.route("/name") #add route for search web2
def hellonink():
    return "Hello, Nink!"

@app.route("/home", methods={'POST'}) #add route for search web
def homefn():
    print('we are in home')
    #getting input with name = fname in HTML form
    namein = request.form.get('fname')
    lastnamein = request.form.get('lname')
    print(namein)
    print(lastnamein) #addinput from web into our html
    return render_template("home.html", name=namein)

if __name__=="__main__": 
    app.run(host='0.0.0.0', debug=True, port=5001) #host=0.0.0.0 :)
