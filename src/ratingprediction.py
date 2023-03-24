from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences

from src.aspectclassification import *


class RatingPrediction:
    __df = pd.DataFrame
    __model = load_model('./models/cnn_model_with_dropout_updated_v2.h5')
    __tokenizer = joblib.load('./models/word_tokenizer_rating_prediction_v2.pkl')
    __max_length = 100

    def __init__(self, url):
        classified = AspectClassification(url)
        self.__df = classified.getdataframe()
        self.__predictrating()
        self.__savetocsv()

    def __predictrating(self):
        data = list(self.__df['text'])

        # Tokenising instance with earlier trained tokeniser
        data_tokenized = self.__tokenizer.texts_to_sequences(data)

        # Pooling instance to have maxlength of 100 tokens
        data_padded = pad_sequences(data_tokenized, padding='post', maxlen=self.__max_length)

        np.asarray(data_padded)

        # Passing tokenised instance to the model for predictions
        pred = self.__model.predict(data_padded)

        self.__df['predicted_rating'] = np.round((pred * 10) / 2, 1)
        # edit this to put 1 if the rating is lower than 1 and
        print(self.__df['predicted_rating'].mean())
        return self.__df

    def __savetocsv(self):
        # self.__df['category'] = pred

        prediction_category = pd.DataFrame(self.__df['category'], columns=['category'])
        prediction_rating = pd.DataFrame(self.__df['predicted_rating'], columns=['predicted_rating'])
        rating = pd.DataFrame(self.__df['rating'], columns=['rating'])
        text = pd.DataFrame(self.__df['text'], columns=['text'])

        dfx = pd.concat([rating, text, prediction_category, prediction_rating], axis=1)
        # self.__df = dfx

        dfx.to_csv("./data/scrapped_category_predicted_new.csv")
        # print(dfx)

    def getrating(self):
        return np.round(self.__df['predicted_rating'].mean(), 1)

    def getfoodrating(self):
        if self.__df['predicted_rating'][self.__df['category'] == 'food'].empty:
            return "No any Recent Reviews related to food category"

        return np.round(self.__df['predicted_rating'][self.__df['category'] == 'food'].mean(), 1)

    def getambiencerating(self):
        if self.__df['predicted_rating'][self.__df['category'] == 'ambience'].empty:
            return "No any Recent Reviews related to ambience category"

        return np.round(self.__df['predicted_rating'][self.__df['category'] == 'ambience'].mean(), 1)

    def getservicerating(self):
        if self.__df['predicted_rating'][self.__df['category'] == 'service'].empty:
            return "No any Recent Reviews related to service category"

        return np.round(self.__df['predicted_rating'][self.__df['category'] == 'service'].mean(), 1)

    def getpricerating(self):
        if self.__df['predicted_rating'][self.__df['category'] == 'price'].empty:
            return "No any Recent Reviews related to price category"

        return np.round(self.__df['predicted_rating'][self.__df['category'] == 'price'].mean(), 1)

    def getotherrating(self):
        if self.__df['predicted_rating'][self.__df['category'] == 'anecdotes/miscellaneous'].empty:
            return "No any Recent Reviews related to anecdotes/miscellaneous category"

        return np.round(self.__df['predicted_rating'][self.__df['category'] == 'anecdotes/miscellaneous'].mean(), 1)
