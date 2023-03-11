import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib
from nltk.stem import WordNetLemmatizer

import re
import nltk

from src.preprocessdata import *

from nltk.corpus import stopwords


class AspectClassification:
    __df = pd.DataFrame
    __clf = joblib.load('./models/aspect_classification_model.pkl')
    __vectorizer = joblib.load('./models/aspect_classification_vectorizer.pkl')

    def __init__(self):
        self.__df = pd.read_csv('./data/scrapped.csv')
        processed = PreprocessData(self.__df)
        self.__df = processed.getdataframe()
        print(self.__df)


