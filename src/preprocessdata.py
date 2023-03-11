import re

import nltk
import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer

# # run once only
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('omw-1.4')


class PreprocessData:
    __df = pd.DataFrame
    __lemmatizer = WordNetLemmatizer()
    __custom_stopwords = [
        'a', 'an', 'the', 'and', 'but', 'or', 'in', 'on', 'at', 'to', 'of', 'for', 'with', 'by',
        'from', 'that', 'this', 'these', 'those', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
        'has', 'had', 'do', 'does', 'did', 'can', 'could', 'may', 'might', 'must', 'shall', 'should',
        'will', 'would', 'her', 'him', 'his', 'it', 'its', 'our', 'ours', 'their', 'theirs', 'us', 'you', 'your',
        'yours'
    ]

    def __init__(self, df):
        self.__df = self.__clean_texts(df)

    def __remove_stopwords(self, text):
        stopwords = set(self.__custom_stopwords)
        text = ' '.join([word for word in text.split() if word.lower() not in stopwords])
        return text

        # Define a function to convert POS tags to WordNet POS tags

    def __get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return 'a'  # Adjective
        elif treebank_tag.startswith('V'):
            return 'v'  # Verb
        elif treebank_tag.startswith('N'):
            return 'n'  # Noun
        elif treebank_tag.startswith('R'):
            return 'r'  # Adverb
        else:
            return 'n'  # Default to noun if no match

    # Define a function to lemmatize a sentence
    def __lemmatize_sentence(self, sentence):
        # Tokenize the sentence
        tokens = nltk.word_tokenize(sentence)

        # Perform POS tagging
        tagged_tokens = nltk.pos_tag(tokens)

        # Lemmatize each word in the sentence
        lemmatized_words = []
        for token, tag in tagged_tokens:
            pos = self.__get_wordnet_pos(tag)
            lemma = self.__lemmatizer.lemmatize(token, pos=pos)
            lemmatized_words.append(lemma)

        # Join the lemmatized words back into a sentence
        lemmatized_sentence = ' '.join(lemmatized_words)
        return lemmatized_sentence

    def __clean_texts(self, df):
        # removing empty values from the dataframe
        df = df.replace('', np.nan)
        df = df.dropna()
        print('dropped null values --successful')

        columns_to_drop = ['name', 'duration']
        df = df.drop(columns=columns_to_drop)
        print('dropped unwanted columns --successful')

        df.rename(columns={'review': 'text'}, inplace=True)
        print('renamed review column --successful')

        print('preprocessing started ...')
        df['text'] = df['text'].str.lower()

        # remove html tags if there are any
        r = re.compile(r'<[^>]+')
        df['text'] = [r.sub('', s) for s in df['text'].tolist()]

        # remove everthing except letters
        r = re.compile(r'[^\w\s]+')
        df['text'] = [r.sub('', s) for s in df['text'].tolist()]

        # remove stopword from the text
        df['text'] = df['text'].apply(self.__remove_stopwords)

        # remove one word sentences
        df = df[[len(i.split()) > 1 for i in df['text'].values]]

        # lemmatize the sentences
        df['lemmatized'] = ''
        df['lemmatized'] = df['text'].apply(lambda x: self.__lemmatize_sentence(x))
        print('finished preprocessing --successful')

        return df

    def getdataframe(self):
        return self.__df
