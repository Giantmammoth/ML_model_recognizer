import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv('./A-Z.csv')

X = data.drop('0', axis=1)
y = data['0']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

RFC = RandomForestClassifier(n_estimators=150)
RFC.fit(X_train, y_train)

ypred = RFC.predict(X_test)
print(RFC, ":", accuracy_score(y_test, ypred) * 100)

# Exporter le modèle en utilisant joblib
joblib.dump(RFC, 'A-Z-recognizing.joblib')
