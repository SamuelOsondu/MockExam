from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("chooseyear.html")


@app.route('/first_year')
def first_year():
    return render_template("yearone.html")


@app.route('/second_year')
def second_year():
    return render_template("yeartwo.html")


if __name__ == '__main__':
    app.config['FLASK_DEBUG'] = 1
    app.run()

