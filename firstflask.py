from flask import Flask, request, render_template, make_response
import sys
import json

app = Flask(__name__) #start server

#api
@app.route("/request", method = {'POST'})
def web_service_API():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)

    print(inmessage)

    json_data = json.dumps({'y': 'received!'})
    return json_data

@app.route("/") #add route for search web1
def helloworld():
    return "Hello, World!"

@app.route("/name") #add route for search web2
def hellonink():
    return "Hello, Nink!"

@app.route("/home2") #add route for search web3
def home2():
    return render_template("home.html", name="nink")

@app.route("/home", methods={'POST','GET'}) #add POST send message inbox and GET to get message from url
def homefn():
    if request.method == "GET":
        print('we are in home(GET)', file=sys.stdout)
        namein = request.args.get('fname')
        print(namein, file=sys.stdout)
        return render_template("home.html", name=namein)

    elif request.method == "POST":
        print('we are in home(POST)', file=sys.stdout)
        namein = request.form.get('fname')
        lastnamein = request.form.get('lname')
        print(namein, file=sys.stdout)
        print(lastnamein, file=sys.stdout)
        return render_template("home.html", name=namein)

@app.route('/upload', methods=['GET', 'POST']) #get and post into return
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        #if 'file' not in request.files:
            #flash('No file part')
            #return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        #if file.filename == '':
            #flash('No selected file')
            #return redirect(request.url)
        file.save('filename')
        return render_template("home.html", name='upload completed')
    
    return '''
    <!doctype html> 
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
if __name__=="__main__": 
    app.run(host='0.0.0.0', debug=True, port=5001) #host=0.0.0.0 :)
