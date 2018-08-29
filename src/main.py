import numpy as np
import pandas as pd

# Hierarchical indexing:

data_series = pd.Series(np.random.randn(9),
                        index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 1, 3, 3, 2, 2, 3, 4, 1]])
print(data_series)