from flask import Flask, render_template, request

from src.aspectclassification import *
from src.scrapedata import ScrapeData

app = Flask(__name__)


@app.route('/')
def display():  # put application's code here
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def predict():
    # url = request.form['url']
    # ScrapeData(url)
    AspectClassification()
    return render_template('index.html', prediction_text="The Data has been downloaded")


if __name__ == '__main__':
    app.run()
