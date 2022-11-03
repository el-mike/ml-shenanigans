from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np

SurvivedPlotData = Tuple[str, List[str], List[List[int]]]

def plot_survived_by_category(plots: List[SurvivedPlotData]) -> None:
  n_cols = 3
  n_rows = (len(plots) // (n_cols + 1)) + 1
  

  fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, (4 * n_rows)))

  # Single bar width.
  width = 0.4
  alpha = 0.7

  for row in range(0, n_rows):
    for col in range(0, n_cols):
      i = (row * n_cols) + col

      if i == len(plots):
        return

      plot = plots[i]
      ax = axes[col] if n_rows == 1 else axes[row][col]
    
      title, labels, counts = plot 
      x = np.arange(len(labels))

      died_counts = [count[0] for count in counts]
      survived_counts = [count[1] for count in counts]

      died_bars = ax.bar(x - width/2, died_counts, width, label='died', color='red', alpha=alpha)
      survived_bars = ax.bar(x + width/2, survived_counts, width, label='survived', color='green', alpha=alpha)

      ax.set_title(title)
      ax.set_ylabel('counts')
      ax.set_xticks(x, labels)
      ax.legend()

      ax.bar_label(died_bars, padding=1)
      ax.bar_label(survived_bars, padding=1)

  fig.tight_layout()

