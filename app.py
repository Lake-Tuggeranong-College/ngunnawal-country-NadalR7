from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, LoginManager, logout_user, login_required

app = Flask(__name__)
app.config.from_object(Config)  # loads the configuration for the database
db = SQLAlchemy(app)  # creates the db object using the configuration
login = LoginManager(app)
login.login_view = 'login'

from forms import ContactForm
from models import Contact

@app.route('/')
def home():  # put application's code here
    return render_template("index.html", title="Homepage")

@app.route('/forums')
def forums():  # put application's code here
    return render_template("forums.html", title="TippyTechnologies Forums")

@app.route('/account')
def account():  # put application's code here
    return render_template("account.html", title="Account")

@app.route("/contactus", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(new_contact)
        db.session.commit()
        # flash("Your message has been sent to administrators.")
        return redirect(url_for("home"))
    return render_template("contactus.html", title="Contact Us", form=form, user=current_user)


if __name__ == '__main__':
    app.run()

