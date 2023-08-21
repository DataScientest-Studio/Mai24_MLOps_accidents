
import sklearn
import pandas as pd 
from sklearn import ensemble
import joblib


X_train = pd.read_csv('data/preprocessed/X_train.csv')
X_test = pd.read_csv('data/preprocessed/X_test.csv')
y_train = pd.read_csv('data/preprocessed/y_train.csv')
y_test = pd.read_csv('data/preprocessed/y_test.csv')

rf_classifier = ensemble.RandomForestClassifier(n_jobs = -1, n_estimators= 100)

#--Train the model
rf_classifier.fit(X_train, y_train)

#--Save the trained model to a file
model_filename = './src/models/trained_model.joblib'
joblib.dump(rf_classifier, model_filename)
print("Model trained and saved successfully.")
