from genericpath import isfile
import os
from typing import Tuple
import pandas as pd
import zipfile

DATA_PATH = os.path.join('datasets')

ZIP_PATH = os.path.join(DATA_PATH, 'titanic.zip')
TRAIN_CSV_PATH = os.path.join(DATA_PATH, 'train.csv')
TEST_CSV_PATH = os.path.join(DATA_PATH, 'test.csv')

class DataLoader:
  def get_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
    if os.path.isfile(ZIP_PATH):
      with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(DATA_PATH)
        os.remove(ZIP_PATH)

    train_set = pd.read_csv(TRAIN_CSV_PATH)
    test_set = pd.read_csv(TEST_CSV_PATH)

    return train_set, test_set
