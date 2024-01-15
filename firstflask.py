from flask import Flask, request, rendor_tamplate, make_response

import json

app = Flask(__name__) #start server

@app.route("/") #add route for search web
def helloworld():
    return "Hello, World!"

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host=0.0.0.0
