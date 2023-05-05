#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 

@app.route("/flask")
def second_webpage():
    return "python is fun"
#run the application on local server

@app.route("/")
def home():
    name = "pinku"
    age = "15"
    
    return render_template("index.html", name = name,age = age)

@app.route("/father")
def home1():
    name2 = "pawan"
    age2 = "41"
    
    return render_template("index.html", name = name2,age = age2)

@app.route("/mother")
def home2():
    name1 = "anju"
    age1 = "38"
    
    return render_template("index.html", name = name2,age = age2)
app.run(debug=True)
