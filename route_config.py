"""
Created on Sun Oct 31 12:23:13 2021

@author: louiemceliberti
"""

# This application will be a website. This will teach me how to create and run a websitw in python ausing Flask

## Flask Code here 
from flask import Flask, flash, render_template, request
#from flask_mysqldb import MySQL
from flask import jsonify
import mysql.connector
app = Flask(__name__)  

"""app.config['MYSQL_HOST'] = 'Louies-MacBook-Pro.local'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Manhattan College'
mysql = MySQL(app)"""

"""mydb = mysql.connect(

  host="127.0.0.1",

  user="root",

  password="Lc654321" 

) """

student = [{'firstname':'Bill','lastname': 'Waters','age':'42'},
            {'firstname':'Karry','lastname': 'Jose','age':'21'},
            {'firstname':'Jess','lastname': 'Prea','age':'53'},
            {'firstname':'Tom','lastname': 'Sanders','age':'19'}]

@app.route("/student",methods=['GET'])
def get_student():
    return jsonify({'task': student})

@app.route("/student", methods=['POST'])
def add_student():
    newstudent = {
        'firstname': request.json['firstname'],
        'lastname': request.json['lastname'],
        'age':request.json['age']
        }
    student.append(newstudent)
    return jsonify({'student':newstudent})

@app.route("/test")
def user():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

@app.route("/")
def welcomeFunction():
    return render_template('Welcome.html')

@app.route("/Routine")
def routineFunction():
    return render_template('Routine.html')

@app.route("/ErrorSolutions")
def errorsolutionFunction():
    return render_template('Solutions.html')

@app.route("/BudgetManagement", methods=['GET','POST'])
def bmfunction():
    return render_template('BudgetManagement.html')

@app.route("/Food/")
@app.route("/Food/<resturants>")
def foodFunction(resturants=None):
    return render_template('Food.html', resturants=resturants)

@app.route("/Fashion/")
@app.route("/Fashion/<shoes>")
def fashionFunction(shoes=None):
    return render_template('Fashion.html', shoes=shoes)

@app.route("/Fitness/")
@app.route("/Fitness/<Calisthetics>")
def fitnessFunction(Calisthetics=None):
    return render_template('Fitness.html', Calisthetics=Calisthetics)



### Educational Page functions: ###
@app.route("/Education/")
def educationFunction():
    return render_template('Education.html')

@app.route("/Education/Psychology/")
@app.route("/Education/Psychology/<behaviorism>")
def psychologyFunction(behaviorism=None):
    return render_template('Psychology.html', behaviorism=behaviorism)

@app.route("/Education/Programming/")
@app.route("/Education/Programming/<ProgrammingTutorials>")
def programmingFunction(ProgrammingTutorials=None):
    return render_template('Programming.html', ProgrammingTutorials=ProgrammingTutorials)    

@app.route("/Education/Cryptocurrency/")
@app.route("/Education/Cryptocurrency/<Bitcoin>")
def cryptoFunction(Bitcoin=None):
    return render_template('Cryptocurrency.html', Bitcoin=Bitcoin)

@app.route("/Education/Finance/")
@app.route("/Education/Finance/<Markets>")
def fincanceFunction(Markets=None):
    return render_template('Cryptocurrency.html', Markets=Markets)

@app.route("/Education/Economics/")
@app.route("/Education/Economics/<GDP>")
def economicsFunction(GDP=None):
    return render_template('Cryptocurrency.html', GDP=GDP)
### End of Educational functions ###

if __name__ == "__main__":  
    app.run(debug=True)