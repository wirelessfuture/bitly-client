import os

from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from url import shorten, expand

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Our main form
class URLForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    method = SelectField(label="Method", choices=[('s', 'Shorten'), ('e', 'Expand')])
    submit = SubmitField('Process')

# Listens to GET requests with required paremeters
# Accepts user input via the web form at 127.0.0.1:5000/
# Uses flasks internal listener for processing form submit
@app.route('/', methods=['GET', 'POST'])
def home():
    # Check if the incoming request contains args
    if len(request.args) > 0:
        method = request.args.get('method')
        url = request.args.get('url')
        if method and url:
            if method == "shorten":
                return {"url": shorten(url)["url_after"]}
            elif method == "expand":
                return {"url": expand(url)["url_after"]}
        else:
            return {"error": "missing required parameters"}
    # If no args, then render user form and listen for submit
    else:
        form = URLForm()
        if form.validate_on_submit():
            method = form.method.data
            if method == "s":
                return {"url": shorten(form.url.data)["url_after"]}
            elif method == "e":
                return {"url": expand(form.url.data)["url_after"]}
        return render_template("home.html", form=form)
    
