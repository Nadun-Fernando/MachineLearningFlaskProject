import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords


class PreprocessData:
    __df = pd.DataFrame

    def __clean_texts(self, df):
        df['text'] = df['text'].str.lower()

        ## remove html tags if there are any
        r = re.compile(r'<[^>]+')
        df['text'] = [r.sub('', s) for s in df['text'].tolist()]

        ## remove everthing except letters
        r = re.compile(r'[^\w\s]+')
        df['text'] = [r.sub('', s) for s in df['text'].tolist()]

        ## remove stopword from the text
        r = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
        df['text'] = [r.sub('', s) for s in df['text'].tolist()]

        return df
