import pandas as pd

df = pd.read_csv('./data/housing.data', header=None, sep='\s+')
df.columns = ["CRIM","ZN","INDUS" ,"CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"]

print(df.head())