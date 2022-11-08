import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin

import common.columns as columns

CHILD_GROUP = 'child'
ADULT_GROUP = 'adult'
SENIOR_GROUP = 'senior'

CHILD_TYPE = 'child'
MAN_TYPE = 'man'
WOMAN_TYPE = 'woman'

class PersonTypeAdder(BaseEstimator, TransformerMixin):
  def __init__(self, adult_age=16, senior_age=56):
    self.adult_age = adult_age
    self.senior_age = senior_age
  
  def fit(self, X: pd.DataFrame, y=None):
    return self

  def transform(self, X: pd.DataFrame, y=None):
    X[columns.AGE_GROUP] = pd.cut(
      X[columns.AGE],
      bins=[0, self.adult_age, self.senior_age, 100],
      labels=[CHILD_GROUP, ADULT_GROUP, SENIOR_GROUP]
    )

    person_types = X.apply(lambda row: self._get_type(row), axis=1)

    X[columns.PERSON_TYPE] = person_types

    return X

  def _get_type(self, row: pd.Series) -> str:
    if row[columns.AGE_GROUP] == CHILD_GROUP:
      return CHILD_TYPE
    else:
      return MAN_TYPE if row[columns.SEX] == 'male' else WOMAN_TYPE
