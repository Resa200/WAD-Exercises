from flask import Flask, render_template

app = Flask(__name__)

@app.get("/fizzbuzz")
def fizzbuzz():
    return render_template("fizzbuzz.html")
