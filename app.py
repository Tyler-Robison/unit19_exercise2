from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickensarecool123456"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('madlibs.html')