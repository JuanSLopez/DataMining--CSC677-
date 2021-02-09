"""
November 10,2020

 Juan Lopez
"""

# Import all the libraries needed
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from time import time
from sklearn.metrics import f1_score
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

# Read the Data
data = pd.read_csv('final.csv')

# Remove the first 3 matches of the week
data = data[data.MW > 3]

# Drop the irrelevant attributes
data.drop(['Unnamed: 0','HomeTeam', 'AwayTeam', 'Date', 'MW', 'HTFormPtsStr', 'ATFormPtsStr', 'FTHG', 'FTAG', 'HTGS', 'ATGS', 'HTGC', 'ATGC','HomeTeamLP', 'AwayTeamLP','DiffPts','HTFormPts','ATFormPts', 'HM4','HM5','AM4','AM5','HTLossStreak5','ATLossStreak5','HTWinStreak5','ATWinStreak5', 'HTWinStreak3','HTLossStreak3','ATWinStreak3','ATLossStreak3'],axis=1, inplace=True)


X_all = data.drop(['FTR'],1)
y_all = data['FTR']

# Normalization of the Data


cols = [['HTGD','ATGD','HTP','ATP','DiffLP']]
for col in cols:
    X_all[col] = scale(X_all[col])
    
X_all.HM1 = X_all.HM1.astype('str')
X_all.HM2 = X_all.HM2.astype('str')
X_all.HM3 = X_all.HM3.astype('str')
X_all.AM1 = X_all.AM1.astype('str')
X_all.AM2 = X_all.AM2.astype('str')
X_all.AM3 = X_all.AM3.astype('str')

def preprocess(X):
    
    # Output dataFrame

    output = pd.DataFrame(index=X.index)

    # Look into each instance for categorical types
    for col, col_data in X.iteritems():

        # one-hot encoding on these objects
        if col_data.dtype == object:
            col_data = pd.get_dummies(col_data, prefix=col)
                    
        # Append it to the output dataframe
        output = output.join(col_data)
    
    return output

X_all = preprocess(X_all)


# Stratify and split data into train and testing
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size = 0.2,random_state = 2,stratify = y_all)

X_train = X_train.to_numpy()
X_test = X_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()



    
def labelPrediction(clf, features, target):
    start = time()
    y_pred = clf.predict(features)
    end = time()
    totaltime = end-start
    print ("Time it took to predict: {:.4f}".format(totaltime))
    return f1_score(target, y_pred, labels=['HOME','DRAW','AWAY'], average = None), sum(target == y_pred) / float(len(y_pred)), clf.score(features, target), y_pred


def trainingClassifier(clf, X_train, y_train):
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    totaltime = end - start
    print("Time it took to train: {:.4f}".format(totaltime))


def printF1Acc(f1, acc):
    newF1 = ((f1[0] + f1[1] + f1[2]) / 3)
    print(newF1, acc)


def predictiveTraining(clf, X_train, y_train, X_test, y_test):
    print ("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)))
    trainingClassifier(clf, X_train, y_train)
    f1, accurac, confidence, _ = labelPrediction(clf, X_train, y_train)
    printF1Acc(f1, accurac)
    f1, accurac, confidence, predictions = labelPrediction(clf, X_test, y_test)
    printF1Acc(f1, accurac)
    return confidence, predictions


# Initialize the three models, train the models, and evaluate

clf_A = LogisticRegression(random_state = 42)
clf_B = SVC(random_state = 912, kernel='rbf')
clf_C = xgb.XGBClassifier(seed = 82)

predictiveTraining(clf_A, X_train, y_train, X_test, y_test)
print('__________________________________________________')
predictiveTraining(clf_B, X_train, y_train, X_test, y_test)
print('__________________________________________________')
predictiveTraining(clf_C, X_train, y_train, X_test, y_test)
print('__________________________________________________')



# Import GridSearchCV and optimize XGBoost model


def gridSearchOptimizer(clf, scoring, param, X_all, y_all):
    gridsearch = GridSearchCV(clf, scoring=scoring, param_grid=param, verbose=100)
    gridObject = gridsearch.fit(X_all,y_all)
    clf = gridObject.best_estimator_
    params = gridObject.best_params_
    print(clf)
    print(params)
    return clf



clf_D = xgb.XGBClassifier()
parameters_D = {'learning_rate': [0.01],'n_estimators':[1000],'max_depth': [2],'min_child_weight': [5],'gamma': [0],'subsample': [0.8],'colsample_bytree': [0.7],'scale_pos_weight':[0.8],'reg_alpha':[1e-5],'booster': ['gbtree'],'objective': ['multi:softprob']}
f1_scorer_D = make_scorer(f1_score, labels=['HOME','DRAW','AWAY'], average = 'micro')
clf_D = gridSearchOptimizer(clf_D, f1_scorer_D, parameters_D, X_train, y_train)


f1, acc, confidence, _ = labelPrediction(clf_D, X_train, y_train)
printF1Acc(f1,acc)
   
    
f1, acc, confidence, predictions = labelPrediction(clf_D, X_test, y_test)
printF1Acc(f1,acc)
