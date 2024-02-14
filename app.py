from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", title="Homepage")

@app.route('/history')
def history():  # put application's code here
    return render_template("history.html", title="History of Ngunnawal")

@app.route('/imagegallery')
def imagegallery():  # put application's code here
    return render_template("imagegallery.html", title="Image Gallery")

@app.route('/contactus')
def contactus():  # put application's code here
    return render_template("contactus.html", title="Contact Us")

if __name__ == '__main__':
    app.run()
