import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

data = pd.read_csv("car_evaluation.csv", header = None)
transactions = []
print(data.shape)
for i in range(0,1729):
    transactions.append([str(data.values[i,j]) for j in range(0,7)])

rules = apriori(transactions=transactions, min_support=.003, min_confidence=0.2, min_lift=3, min_length=0, max_length=4)
results = list(rules)
print(results)

'''
def inspect(results):
    lhs =[tuple(result[2][0][0])[0] for result in results]
    rhs =[tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs,rhs,supports,confidences,lifts))

resultsinDataFrame = pd.DataFrame(inspect(results),columns = ["Left Hand Side","Right Hand Side", "Support","Confidence", "Lifts"])
resultsinDataFrame.to_csv("Results.csv",index=False, header = True)
'''
for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
