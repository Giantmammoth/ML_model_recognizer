import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib

path = './CompleteImages/All data (Compressed)/'
tab = []
for i, folder in enumerate(os.listdir(path)):
    for j, file in enumerate(os.listdir(os.path.join(path, folder))):
        im = Image.open(os.path.join(path, folder, file))
        im = im.convert('L')
        im = im.resize((28, 28))
        im = im.filter(ImageFilter.SMOOTH)
        im = np.ravel(im)
        im = np.append(im, [i])
        tab.append(im)

tab = np.array(tab)

data = pd.DataFrame(tab)
data.iloc[:, :-1] = data.iloc[:, :-1].apply(func= lambda x: 255-x)

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

RFC = RandomForestClassifier(n_estimators=150)
RFC.fit(X_train, y_train)

ypred = RFC.predict(X_test)
print(RFC, ":", accuracy_score(y_test, ypred) * 100)

# Exporter le modèle en utilisant joblib
joblib.dump(RFC, 'sym-num-recognizing.joblib')