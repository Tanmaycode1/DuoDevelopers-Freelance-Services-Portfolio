from flask import render_template,flash,Flask,request
import sqlite3
from mails import *

con = sqlite3.connect("userinfo.db",check_same_thread=False)
cur = con.cursor()

cur.execute("create table if not exists inquiries( nam varchar,email varchar,contact varchar ,subject varchar)")

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"

@app.route('/',methods=['GET', 'POST'])
def home():
  if request.method == "POST":
       nam = request.form.get('name')
       email = request.form.get('email')
       contact = request.form.get('number')
       subject = request.form.get('subject')
       print(nam)

       cur.execute("insert into inquiries values('{}','{}','{}','{}')".format(nam,email,contact,subject))
       con.commit()

       mailtoclient(email,nam)
       mailtoourself(email,nam,contact,subject)
       flash("Thanks For your interest We'll Contact you soon",category="success")


  return render_template("index.html")

@app.route('/aditya')
def aditya():
    return "<center><h1><font size='7'>Aditya</font></h1><br><h1>Portfolio Under Construction</h1></center>"

@app.route('/tanmay')
def tanmay():
     return render_template("tanmay.html")
@app.route('/requests')
def requests():
     cur.execute("select * from inquiries")
     row = cur.fetchall()
     return render_template("requests.html",rows=row)


if __name__ == '__main__':
    app.run(debug=True)