# Decision Tree Classifier

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus


# Create a dataframe from dataset

data = pd.read_csv("IntegerCarEvaluation.csv")

#Print first 5 rows

print(data.head())

#Total Length of data

print(len(data))

#Split the data into independent and dependent
#Gets all rows from buying to safety

xTrain = data.loc[:,"buying":"safety"]

#Gets all the class labels

yTrain = data.loc[:,"class"]


#Split data
x_train, x_test, y_train, y_test = train_test_split(xTrain,yTrain,test_size=0.6,random_state=0)



#Create Decision Tree Classifier

tree = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)

# Train the Model

tree.fit(x_train,y_train)



#Make prediction
# Input: buying = vhigh, maint = high, doors = 2, persons = 6, lug_boot = med, safety = high
prediction = tree.predict(x_test)

#Print prediction

print(prediction)


#Print Accuracy

print("Accuracy:", metrics.accuracy_score(y_test, prediction))


col_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety"]

dot_data = StringIO()
export_graphviz(tree, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = col_names,class_names=["unacc","acc","good","vgood"])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("DTcar.png")
Image(graph.create_png())
