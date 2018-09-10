from flask import render_template
from . import main
from flask_login import login_required


@main.route('/')
@login_required
def index():
    """
    View root page function that returns the index page and its data
    """
    title = "Welcome to  your best Pitches || pitch it now !"
    return render_template('index.html', title = title)

