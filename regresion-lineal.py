import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./data/housing.data', header=None, sep='\s+')
df.columns = ["CRIM","ZN","INDUS" ,"CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"]

print(df.head())

sns.set(style='whitegrid', context='notebook')

cols = ["DIS", "INDUS", "CRIM", "RM", "MEDV"]

sns.pairplot(df[cols], height=2.5)
plt.show()

#cm = np.corrcoef(df[cols])
cm = np.corrcoef(df[cols].values.T)

sns.set(font_scale=1.5)
sns.heatmap(cm, cbar=True, annot=True, yticklabels=cols,xticklabels=cols, cmap='coolwarm')
#sns.heatmap(df[cols].corr(), annot= True, cmap='coolwarm')
plt.show()