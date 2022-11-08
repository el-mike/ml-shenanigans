import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin

import common.columns as columns

class ColumnDropper(BaseEstimator, TransformerMixin):
  def __init__(self, columns: list[str]):
    self.columns = columns

  def fit(self, X: pd.DataFrame, y=None):
    return self

  def transform(self, X: pd.DataFrame, y=None):
    return X.drop(self.columns, axis=1)
