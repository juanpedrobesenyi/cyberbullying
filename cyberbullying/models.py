import numpy as np
import pandas as pd
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

from cyberbullying.utils import preprocess_x
from cyberbullying.transformers import CleanDFTransformer

import joblib


class MLModel:
    def __init__(self, **kwargs):
        self.path_file = os.path.dirname(__file__) # no funciona en jupyter
        if kwargs is None:
            kwargs = dict()
        min_df = kwargs.get('min_df', 3)
        max_df = kwargs.get('max_df', 1.0)
        max_features = kwargs.get('max_features', None)
        C = kwargs.get('C', 1)
        class_weight_0 = kwargs.get('class_weight_0', 0.20)
        class_weight = {0:class_weight_0, 1:1-class_weight_0}
        penalty = kwargs.get('penalty', 'l1')
        loss = kwargs.get('loss', 'squared_hinge')
        dual = kwargs.get('dual', False)

        self.vectorizer = TfidfVectorizer(
            min_df=min_df,
            max_df=max_df,
            max_features=max_features
        )

        self.model = LinearSVC(
            C=C,
            class_weight=class_weight,
            penalty=penalty,
            loss=loss,
            dual=dual
        )

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
        X_test = preprocess_x(X_test)
        y_pred = self.pipeline.predict(X_test)
        return y_pred

    def predict_proba(self, X_test):
        X_test = preprocess_x(X_test)
        X_test_vec = self.pipeline.steps[:-1][0][1].transform(X_test)
        y_pred_proba = self.model._predict_proba_lr(X_test_vec)
        return y_pred_proba

    def predict_all(self, X_test):
        X_test = preprocess_x(X_test)
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
            (df['proba_1'] <= 0.85),
            (df['proba_1'] <= 1.0)
            ]

        # create a list of the values we want to assign for each condition
        values = [None, 'yellow', 'orange', 'red']

        # create a new column and use np.select to assign values to it using our lists as arguments
        df['color'] = np.select(conditions, values)

        return df

    def predict_simple_text(self, X_test):
        X_test = X_test.split()
        df = self.predict_all(X_test)
        return df

    def predict_phrase(self, X_test, split=None):
        prediction = self.predict(X_test)
        html_phrase = ''
        if prediction == 0.0:
            html_phrase = None
        else:
            df = self.predict_simple_text(X_test)
            for text, color in zip(df['text'], df['color']):
                if color == None:
                    html_phrase += f'{text} '
                else:
                    html_phrase += f'<{color}>{text}</{color}> '
            html_phrase = html_phrase.strip()
        output = {'prediction': prediction[0], 'text': html_phrase}
        return output

    # no se usa
    def save_model(self):
        """ Save the trained model into a model.joblib file """
        #path_file = os.path.dirname(__file__) # no funciona en jupyter
        joblib.dump(self.pipeline, self.path_file+'/../model0.joblib')




class MLClassifier:
    def __init__(self, **kwargs):
        self.path_file = os.path.dirname(__file__) # no funciona en jupyter
        if kwargs is None:
            kwargs = dict()
        min_df = kwargs.get('min_df', 10)
        max_df = kwargs.get('max_df', 0.8)
        max_features = kwargs.get('max_features', 25000)
        ngram_range = kwargs.get('ngram_range', (1,2))
        max_depth = kwargs.get('max_depth', 3)
        n_estimators = kwargs.get('n_estimators', 10)


        self.vectorizer = TfidfVectorizer(
            min_df=min_df,
            max_df=max_df,
            max_features=max_features,
            ngram_range=ngram_range
        )

        self.model = AdaBoostClassifier(
            DecisionTreeClassifier(
                max_depth=max_depth
            ),
            n_estimators=n_estimators
        )

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
        label_enc = LabelEncoder()
        y_train_encoded = label_enc.fit_transform(y_train)
        self.pipeline.fit(X_train, y_train_encoded)
        self.class_labels = label_enc.classes_

    def predict(self, X_test):
        X_test = preprocess_x(X_test)
        y_pred_encoded = self.pipeline.predict(X_test)
        y_pred = [self.class_labels[y] for y in y_pred_encoded]
        return y_pred
