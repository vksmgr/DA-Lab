import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# bar graph with dataframes
fig, axes = plt.subplots(1,1)
data_frame = pd.DataFrame(np.random.rand(6,4),
                          index=['one', 'two', 'three', 'four', 'five', 'six'],
                          columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
data_frame.plot.barh( stacked=True, alpha=0.5)
plt.show()

##ploting with pandas and seaborn

tips = pd.read_csv('/home/vikas/DA/Dy-Py/data/tips.csv')

party_counts = pd.crosstab(tips['day'], tips['size'])

print(party_counts)
party_counts = party_counts.loc[:, 2:5]
print(party_counts)

# normalizing so that sum to 1
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
print(party_pcts)
party_pcts.plot.bar()
plt.show()
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

sns.barplot(x='tip_pct', y='day',hue='time', data=tips, orient='h')
sns.set(style="whitegrid")
plt.show()