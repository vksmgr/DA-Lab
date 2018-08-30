import numpy as np
import pandas as pd

# Hierarchical indexing:

data_series = pd.Series(np.random.randn(9),
                        index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data_series)

# to see which type of the index it is using you
print(data_series.index)

# Indexing the multilevel

print(data_series['a', 1])

#converting series to the Dataframe
print(data_series.drop_duplicates().unstack())

#converting a dataframe to a series
data_frame = pd.DataFrame(np.random.randn(9).reshape((3,3)))
print(data_frame)
print(data_frame.stack())       # simply this method will use the multilevel indexin to convert dataframe to series

#naming hierarchy
data_series.index.names = ['Level 1', 'Level 2']
print(data_series)


#if you want to swap the level's only then we can use swaplevel()
# sorting index leel by level sort_index() will take the level and sort the data in that level
print(data_series.sort_index(level=0)) # data is sorted according o this level

print(data_series.swaplevel(1,0))

#summary statistics
print(data_series.sum(level='Level 2'))


#Indexing through Columns
print('============================================Column indexing==================')

print(data_frame)

print(data_frame.set_index([0, 1], drop=False))
print(data_frame.reset_index())

#######
# Performing Join On Data : mergin Files
#######

data_frame_1 = pd.DataFrame({'Key':[ 'b', 'b', 'a', 'c', 'a', 'a', 'b'],
                             'data1': range(7)})

data_frame_2 = pd.DataFrame({'Key': ['a', 'b', 'c'],
                             'data2': range(3)})

# Performing Merge
print(data_frame_1)
print(data_frame_2)

print(pd.merge(data_frame_1,data_frame_2, on='Key', how='inner', indicator=True))

## Join on Hierarchical indexed data

lefth = pd.DataFrame({'key1': ['MH', 'TN', 'GOA', 'UP', 'MP'], 'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6,2)),
                      index=[['MH', 'MH','GOA', 'GOA', 'GOA','HP'],[2001, 2000, 2000, 2000, 2001, 2000]],
                      columns=['event1', 'event2'])
print(lefth)

print(righth)



print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'))

left2 = pd.DataFrame([[7,8], [9,2],[3,4]],
                     index=['a', 'b', 'c'],
                     columns=['MH', 'DH'])
right2 = pd.DataFrame([[1, 2], [3, 4], [5, 6]],
                      index=['a', 'e', 'd'],
                      columns=['PJ','GU'])

print(left2)
print(right2)

print(left2.join(right2 , how='outer'))


### Concatination Stacking Or Binding

np_array = np.arange(12).reshape((3,4))
print(np_array)

print(np.concatenate([np_array, np_array], axis=1))

a = pd.Series([np.nan, 2.5, np.nan, 3.4, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series(np.arange(len(a), dtype= np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])

print(a)
print(b)
b[-1] = np.nan
print(b)



#Combing data with overlapping

series_1 = pd.Series(np.arange(10))
series_2 = pd.Series(np.random.randn(10))
series_1[3] = np.nan
series_2[5] = np.nan
print(series_1)
print(series_2)

# combinig with overlapping

#print(pd.merge(series_2, series_1))

print(np.where(pd.isnull(series_1), series_2, series_1))


#combining with dataframes

df1 = pd.DataFrame({'a' : [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})

print(df1)
print(df2)

# ti will not change the value if the both overlapping columns contains the same values
print(df1.combine_first(df2))


# convering data from row to column and column to row's
print(df2.stack())
print(data_series.unstack())

# to unstack the data form the series it must be multiindexed

print(data_series.index)


data2 = pd.concat([series_1, series_2], keys=['one', 'two'])

print(data2.unstack())

print(data2.unstack().stack(dropna=False))








