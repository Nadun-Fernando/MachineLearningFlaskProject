from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS

from src.ratingprediction import *

app = Flask(__name__)


# CORS(app)


@app.route('/')
def display():  # put application's code here
    url = request.args.get('url')
    return render_template('index.html', url=url)


@app.route('/classify', methods=['POST'])
def predict():
    url = request.form['url']
    print(url)
    prediction = RatingPrediction(url)
    rating = prediction.getrating()
    food = prediction.getfoodrating()
    service = prediction.getservicerating()
    ambience = prediction.getambiencerating()
    price = prediction.getpricerating()
    anecdotes = prediction.getotherrating()
    return render_template('results.html',
                           overallrating=rating,
                           foodrating=food,
                           servicerating=service,
                           ambiencerating=ambience,
                           pricerating=price,
                           anecdotesrating=anecdotes
                           )


if __name__ == '__main__':
    app.run()
