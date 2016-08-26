import csv
import os
from sklearn import tree
from sklearn.cross_validation import train_test_split

# open the waveform data file obtained from the website:
# <http://archive.ics.uci.edu/ml/datasets/Waveform+Database+Generator+(Version+2)>
f=open("/Users/nuh-ufmg/Downloads/waveform.data")

line_read=[]

#read the file and capture all the lines in an arrray
for row in csv.reader(f):
    z=[]
    for elem in row:
        z.append(float(elem))
        line_read.append(z)

#capture the input data in the array
X = [l[0:21] for l in line_read]
#capture the output data, the class information
Y = [l[-1] for l in line_read]

#split the data in train and test values
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.3, random_state=10)

#create a decision tree to classify the waveforms. The tree was pruned in order to keep only the eight more significant
#leafs
clf = tree.DecisionTreeClassifier(max_leaf_nodes=10)

#train the decision tree and show the score of the process in order to judge the quality of the prediction.
print(clf.fit(X_train, Y_train).score(X_test, Y_test))

#export tree in a representation form
tree.export_graphviz(clf, out_file='tree.dot',feature_names=None,class_names=["0","1","2"])

#print the graph of the tree
os.system("dot -Tpng -oTree.png -v tree.dot")
