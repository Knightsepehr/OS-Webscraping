from flask import Flask, render_template
from db import connection,close_connection


app = Flask(__name__,template_folder='templates')
jobs = []
# print(jobs[0])
@app.route('/')
def index():
    return render_template("index.html",title="Home",jobs=jobs)

app.run()