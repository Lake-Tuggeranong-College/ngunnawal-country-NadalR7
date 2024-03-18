from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html", title="Homepage")

@app.route('/forums')
def forums():  # put application's code here
    return render_template("forums.html", title="TippyTechnologies Forums")

@app.route('/account')
def account():  # put application's code here
    return render_template("account.html", title="Account")

@app.route('/contactus')
def contactus():  # put application's code here
    return render_template("contactus.html", title="Contact Us")

if __name__ == '__main__':
    app.run()
