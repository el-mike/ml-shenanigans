import re

import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin

import common.columns as columns

TITLE_REGEX = ',\s+(.*?)\s'

class TitleAdder(BaseEstimator, TransformerMixin):
  def fit(self, X: pd.DataFrame, y=None):
    return self

  def transform(self, X: pd.DataFrame, y=None):
    titles = X[columns.NAME].apply(lambda x: self._get_title(x))

    X[columns.TITLE] = titles

    return X

  def _get_title(self, name: str) -> str:
    m = re.search(TITLE_REGEX, name)

    return (m.group(1) if m else None)
