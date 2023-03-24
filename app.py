from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from src.ratingprediction import *

app = Flask(__name__)
CORS(app)
# @app.route('/')
# def display():  # put application's code here
#     return render_template('index.html')


@app.route('/classify', methods=['POST'])
def predict():
    url = request.json['text']
    print(url)
    prediction = RatingPrediction(url)
    rating = prediction.getrating()
    food = prediction.getfoodrating()
    service = prediction.getservicerating()
    ambience = prediction.getambiencerating()
    anecdotes = prediction.getotherrating()
    return jsonify({
        'overall': str(rating),
        'food': str(food),
        'service': str(service),
        'ambience': str(ambience),
        'anecdotes': str(anecdotes)
    })


if __name__ == '__main__':
    app.run()
