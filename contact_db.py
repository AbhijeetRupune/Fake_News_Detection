
from flask import Flask,  request, redirect, render_template, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='techconnect'
mysql = MySQL(app)

@app.route('/add_contact', methods=['GET','POST'])
def add_contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact (name, email, subject, message) VALUES (%s, %s, %s, %s)", (name, email, subject, message))
        mysql.connection.commit()
        return "Thanks For Contact With Us"
    
@app.route('/index', methods=['GET','POST'])
def index():
    add_contact()
    return render_template("index.html")
