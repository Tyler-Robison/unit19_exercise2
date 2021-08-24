from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickensarecool123456"

debug = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route('/')
def home_page():

    words = story.prompts

    return render_template('madlibs.html', my_words=words)

@app.route('/story')
def generate_story():

    test_dict = {}

    for (key, value) in request.args.items():
        test_dict[key] = value

    msg = story.generate(test_dict)

    return render_template('story.html', my_list = msg)    