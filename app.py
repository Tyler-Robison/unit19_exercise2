from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

#We are currently importing story instance not Story Class.

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickensarecool123456"

debug = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# story.prompt
# story.generate()
# As explained in e-mail, I can't access story methods/attrs in global scope, only function scope
# That is why I have the class instantiated inside my functions instead of global scope.

@app.route('/')
def home_page():


    story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

    words = story.prompts
    story
    return render_template('madlibs.html', my_words=words)

@app.route('/story')
def story():

    story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
    test_dict = {}

    for (key, value) in request.args.items():
        test_dict[key] = value

    msg = story.generate(test_dict)

    return render_template('story.html', my_list = msg)    