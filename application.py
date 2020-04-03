import os
import smtplib
from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods= ["POST"])
def register():
    name = request.form.get("Name")
    last = request.form.get("Last Name")
    email = request.form.get("Email")
    phone = request.form.get("Phone")
    message = request.form.get("Message")
    if not email:
        return "faliure"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("mayankae21@gmail.com","***********")
    server.sendmail("mayankae21@gmail.com", email, message)
    return render_template("success.html")
