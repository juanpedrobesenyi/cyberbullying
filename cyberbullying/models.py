import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, make_scorer

from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

from cyberbullying.utils import clean_df
from cyberbullying.transformers import CleanDFTransformer

import joblib


class MLModel:
    def __init__(self, **kwargs):
        if kwargs is None:
            kwargs = dict()
        min_df = kwargs.get('min_df', 3) # poner 3
        max_df = kwargs.get('max_df', 1.0)
        max_features = kwargs.get('max_features', None)
        C = kwargs.get('C', 1)
        class_weight_0 = kwargs.get('class_weight_0', 0.22)
        class_weight = {0:class_weight_0, 1:1-class_weight_0}
        penalty = kwargs.get('penalty', 'l1')
        loss = kwargs.get('loss', 'squared_hinge')
        dual = kwargs.get('dual', False)

        self.vectorizer = TfidfVectorizer(min_df=min_df,
                                          max_df=max_df,
                                          max_features=max_features)

        self.model = LinearSVC(C=C,
                        class_weight=class_weight,
                        penalty=penalty,
                        loss=loss,
                        dual=dual)

    def set_pipeline(self):

        text_prep = make_pipeline(CleanDFTransformer(),
                                      self.vectorizer)

        preprocessing = make_column_transformer(
            (text_prep, ['text']))

        self.pipeline = make_pipeline(
            preprocessing,
            self.model
        )

    def train(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    def predict(self, X_test):
        y_pred = self.pipeline.predict(X_test)
        return y_pred

    def predict_proba(self, X_test):
        X_test_vec = self.pipeline.steps[:-1][0][1].transform(X_test)
        y_pred_proba = self.model._predict_proba_lr(X_test_vec)
        return y_pred_proba

    def predict_all(self, X_test):
        #X_test = preprocess_x(X_test)
        y_pred = self.predict(X_test)
        y_pred_proba = self.predict_proba(X_test)
        color = ['red' if proba==1 else None for proba in y_pred]
        df = pd.DataFrame({'text': X_test['text'],
                           'proba_0': y_pred_proba[:,0],
                           'proba_1': y_pred_proba[:,1],
                           'prediction': y_pred,
                           'color': color})


        # create a list of our conditions
        conditions = [
            (df['proba_1'] <= 0.5),
            (df['proba_1'] <= 0.65),
            (df['proba_1'] <= 0.88),
            (df['proba_1'] <= 1.0)
            ]

        # create a list of the values we want to assign for each condition
        values = [None, 'yellow', 'orange', 'red']

        # create a new column and use np.select to assign values to it using our lists as arguments
        df['color'] = np.select(conditions, values)

        return df

    def predict_simple_text(self, X_test):
        X_test = X_test.split()
        return self.predict_all(X_test)
