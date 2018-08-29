
## Hierarchical Indexing :
   - It will allow you to have multiple indexes to work with.
   
a  1   -0.661052
   1    1.141471
   3   -0.279373
b  3   -0.871816
   2    2.767949
c  2    0.781526
   3    0.235020
d  4    0.992676
   1    1.044627
   
Like this.
```angular2html

data_series = pd.Series(np.random.randn(9),
                        index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 1, 3, 3, 2, 2, 3, 4, 1]])
print(data_series)
```