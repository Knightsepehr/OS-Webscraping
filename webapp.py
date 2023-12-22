from flask import Flask, render_template
from db import connection,close_connection

db = connection("meow")
def query():
    cur = db.cursor()
    cur.execute('SELECT * FROM image2')
    return cur.fetchall()
        


app = Flask(__name__,template_folder='templates')
jobs = query()
# print(jobs[0])
@app.route('/')
def index():
    return render_template("index.html",title="Home",jobs=jobs)

app.run()