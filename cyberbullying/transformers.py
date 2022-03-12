import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator
from cyberbullying.utils import clean_df

class CleanDFTransformer(TransformerMixin, BaseEstimator):
    # BaseEstimator generates get_params() and set_params() methods that all pipelines require
    # TransformerMixin creates fit_transform() method from fit() and transform()

    def __init__(self):
        pass

    def fit(self, X, y=None):
        # Store here what needs to be stored during .fit(X_train) as instance attributes.
        # Return "self" to allow chaining .fit().transform()
        return self

    def transform(self, X, y=None):
        assert isinstance(X, pd.DataFrame)
        # Return result as dataframe for integration into ColumnTransformer
        X = X.copy()
        X =  clean_df(X)
        return X['text']
