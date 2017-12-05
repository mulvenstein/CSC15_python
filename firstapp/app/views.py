from app import app
from flask import request, session, render_template

@app.route('/')
def index():
    return "Hello. This is the index page."

app.secret_key = '324iu234oiu124iu214io12u42i214iou12'
