import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

bankdata = pd.read_csv("bill_authentication.csv")
ret1 = bankdata.shape
print(ret1)

ret2 = bankdata.head
print(ret2)

X = bankdata.drop("Class",axis=1)
Y = bankdata["Class"]
data_train,data_test,target_train,target_test = train_test_split(X,Y,test_size=0.5)

svcclassifier = SVC(kernel='linear')
svcclassifier.fit(data_train,target_train)
predict_clf = svcclassifier.predict(data_test)
print(predict_clf)
print(classification_report(target_test,predict_clf))