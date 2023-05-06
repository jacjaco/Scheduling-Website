from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect)
from model import connect_to_db, db, User
import datetime
import calendar
# import crud
# from mathjax import typeset
import os

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/search')
def search():
    # create a calendar
    calView = calendar.month(2023,5)
    return render_template('search.html', calView = calView)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['action'] == 'signin':
            username = request.form['username']
            email = request.form['email']
            user = User.query.filter_by(email=email).first()
            if user is not None:
                error = "This email is already taken."
                return render_template('login.html', error=error)
            else:
                new_user = User(email=email)
                db.session.add(new_user)
                db.session.commit()
                session['email'] = email
                return redirect('/search')
    return render_template('login.html')

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    connect_to_db(app)
    
    app.run(debug=True, host="0.0.0.0")