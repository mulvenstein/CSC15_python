from app import app
from flask import request, session, render_template

@app.route('/')
def index():
    return "Hello. This is the index paage."

@app.route('/ttt')
def ttt():
    board = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}

    return render_template("tictac.html",board=board)


app.secret_key = '324iu234oiu124iu214io12u42i214iou12'
