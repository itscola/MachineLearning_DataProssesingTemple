import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.impute import SimpleImputer
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.preprocessing import LabelEncoder

Dataset = pd.read_csv('Data.csv')
X = Dataset.iloc[:,:-1].values
y = Dataset.iloc[:,-1].values


# imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# imputer.fit(X[:, 1:3])
# X[:, 1:3] = imputer.transform(X[:, 1:3])


# ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
# X = np.array(ct.fit_transform(X))


# le = LabelEncoder()
# y = le.fit_transform(y)

X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=16)



