from typing import List

import pandas as pd

import common.columns as columns

def get_frequency(target, all):
  return round((100 * (float(target) / float(all))), 0)

def get_survived_counts(
  data: pd.DataFrame,
  filters: List[pd.Series],
  normalize: bool = False
):
  """
  Returns a counts where single count is a pair of died/survived values for
  given filters.

  : param bool normalize: If True, the values will be the relative frequencies.
  """
  counts = []

  for filter in filters:
    # It uses boolean indexing with combined conditions to get the counts pair.
    died = len(data[columns.SURVIVED][filter & (data[columns.SURVIVED] == 0)])
    survived = len(data[columns.SURVIVED][filter & (data[columns.SURVIVED] == 1)])

    if normalize:
      all = len(data[columns.SURVIVED][filter])
      counts.append([get_frequency(died, all), get_frequency(survived, all)])
    else:
      counts.append([died, survived])

  return counts
