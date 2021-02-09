import pandas as pd

#Create File Handler
file_handler = open("car_evaluation.csv","r")

#Create Panda DataFram using read_csv function

data = pd.read_csv(file_handler, sep=",")

#close file
file_handler.close()


#traverse through buying.
#(vhigh,high,med,low) = (4,3,2,1)


data.buying[data.buying == "low"] = 1
data.buying[data.buying == "med"] = 2
data.buying[data.buying == "high"] = 3
data.buying[data.buying == "vhigh"] = 4

#traverse through maint.
#(vhigh,high,med,low) = (4,3,2,1)

data.maint[data.maint == "low"] = 1
data.maint[data.maint == "med"] = 2
data.maint[data.maint == "high"] = 3
data.maint[data.maint == "vhigh"] = 4


#traverse through doors.
#(2,3,4,5more) = (2,3,4,5)

data.doors[data.doors == "5more"] = 5

#traverse through doors.
#(2,4,more) = (2,4,6)

data.persons[data.persons == "more"] = 6

#traverse through lug_boot.
#(small,med, big) = (1,2,3)

data.lug_boot[data.lug_boot == "small"] = 1
data.lug_boot[data.lug_boot == "med"] = 2
data.lug_boot[data.lug_boot == "big"] = 3

#traverse through lug_boot.
#(low,med, high) = (1,2,3)

data.safety[data.safety == "low"] = 1
data.safety[data.safety == "med"] = 2
data.safety[data.safety == "high"] = 3


#Write dataframe to csv file
data.to_csv("IntegerCarEvaluation.csv")