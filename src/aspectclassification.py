import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib

from src.preprocessdata import *


class AspectClassification:
    __df = pd.DataFrame
    __clf = joblib.load('./models/aspect_classification_model.pkl')
    __vectorizer = joblib.load('./models/aspect_classification_vectorizer.pkl')

    def __init__(self):
        self.__df = pd.read_csv('./data/scrapped.csv')
        processed = PreprocessData(self.__df)
        self.__df = processed.getdataframe()
        category_predictions = self.__predictaspect()
        self.__savetocsv(category_predictions)
        # print(self.__df)

    def __predictaspect(self):
        data = list(self.__df['lemmatized'])
        # unseen_reviews

        data_transformed = self.__vectorizer.transform(data)

        # Passing tokenised instance to the model for predictions
        pred = self.__clf.predict(data_transformed)

        return pred

    def __savetocsv(self, pred):
        self.__df['category'] = pred

        prediction_category = pd.DataFrame(self.__df['category'], columns=['category'])
        rating = pd.DataFrame(self.__df['rating'], columns=['rating'])
        text = pd.DataFrame(self.__df['text'], columns=['text'])

        dfx = pd.concat([rating, text, prediction_category], axis=1)

        dfx.to_csv("./data/scrapped_category_predicted.csv")
        print(dfx)

