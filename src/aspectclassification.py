import joblib

from src.preprocessdata import *
from src.scrapedata import *


class AspectClassification:
    __df = pd.DataFrame
    __clf = joblib.load('./models/aspect_classification_model.pkl')
    __vectorizer = joblib.load('./models/aspect_classification_vectorizer.pkl')

    def __init__(self, url):
        scrapped = ScrapeData(url)
        self.__df = scrapped.getdataframe()
        processed = PreprocessData(self.__df)
        self.__df = processed.getdataframe()
        self.__predictaspect()
        # self.__savetocsv(category_predictions)
        # print(self.__df)

    def __predictaspect(self):
        data = list(self.__df['lemmatized'])
        # unseen_reviews

        data_transformed = self.__vectorizer.transform(data)

        # Passing tokenised instance to the model for predictions
        pred = self.__clf.predict(data_transformed)

        self.__df['category'] = pred

        return self.__df

    # def __savetocsv(self, pred):
    #     self.__df['category'] = pred
    #
    #     # prediction_category = pd.DataFrame(self.__df['category'], columns=['category'])
    #     # rating = pd.DataFrame(self.__df['rating'], columns=['rating'])
    #     # text = pd.DataFrame(self.__df['text'], columns=['text'])
    #     #
    #     # dfx = pd.concat([rating, text, prediction_category], axis=1)
    #     # self.__df = dfx
    #     #
    #     # dfx.to_csv("./data/scrapped_category_predicted.csv")
    #     print(self.__df)
    #     return self.__df

    def getdataframe(self):
        return self.__df
