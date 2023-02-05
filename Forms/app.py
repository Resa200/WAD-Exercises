from flask import Flask, request, render_template
import sqlite3

def connect_db():
    db = sqlite3.connect("data.sqlite")
    db.execute('CREATE TABLE IF NOT EXISTS "response" ("name", "engg", "teach", "env","avg")')
    db.commit()
    return db

app = Flask(__name__)

@app.get("/")
def display():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form['fname'] + " " + request.form['lname']
        engg = request.form['engagement']
        teach = request.form['teaching']
        env = request.form['environment']

        score = int(engg) + int(teach) + int(env)
        avg = round(score/3,2)

        db = connect_db()
        #c = db.cursor()
        db.execute("INSERT INTO response (name, engg, teach, env, avg) VALUES (?,?,?,?,?)", (name, engg, teach, env, avg))
        db.commit()
        db.close()
        return render_template("output.html", name=name, engg=engg, teach=teach, env=env, avg=avg)
    else:
        return render_template("form.html")