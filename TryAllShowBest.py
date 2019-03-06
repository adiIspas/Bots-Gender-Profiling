import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap

from sklearn.preprocessing import normalize

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import NearestCentroid

models = []
# models.append(('LR', LogisticRegression()))
# models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('Knn1',     KNeighborsClassifier(1) ))
models.append(('Knn3',     KNeighborsClassifier(3) ))
models.append(('Knn5',     KNeighborsClassifier(5) ))
models.append(('Knn1D',     KNeighborsClassifier(1, weights='distance') ))
models.append(('Knn3D',     KNeighborsClassifier(3, weights='distance') ))
models.append(('Knn5D',     KNeighborsClassifier(5, weights='distance') ))
models.append(('Knn7D',     KNeighborsClassifier(7, weights='distance') ))
models.append(('Knn9D',     KNeighborsClassifier(9, weights='distance') ))
models.append(('Knn11D',     KNeighborsClassifier(11, weights='distance') ))
models.append(('Knn13D',     KNeighborsClassifier(13, weights='distance') ))
# models.append(('LSVM',     SVC(kernel="linear")  ))
# models.append(('RBF',     SVC()  ))
# models.append(('DT',     DecisionTreeClassifier(max_depth=5) ))
# models.append(('RF',     RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1) ))
# models.append(('NN',     MLPClassifier(alpha=1) ))
# models.append(('AB',     AdaBoostClassifier() ))
# models.append(('NB',     GaussianNB() ))
# models.append(('QDA',     QuadraticDiscriminantAnalysis()  ))


#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
#todo, sa vad vecinii aia naspa


# f = open("x_features.txt")
# Features=f.readline().split(',')
# data = np.loadtxt(f,delimiter=",")
# Y=data[:,0]
# X=data[:,1:]
# Features.pop(0)#Primu e clasa

f = open("train.csv")
Features=f.readline().split(',')
data = np.loadtxt(f,delimiter=",")
Features.pop(-1)#ultimu e clasa
Y=data[:,-1]
X=data[:, :-1]
Y= np.transpose([ round(x/2.0+0.1) for x in Y])

# f = open("trainGender.csv")#asta are doar 1 si 2 (deci nu sunt in csv boti)
# Features=f.readline().split(',')
# data = np.loadtxt(f,delimiter=",")
# Features.pop(-1)#ultimu e clasa
# Y=data[:,-1]
# X=data[:, :-1]
# Y= np.transpose([ x-1 for x in Y])


#https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html
from sklearn.ensemble import ExtraTreesClassifier
forest = ExtraTreesClassifier(n_estimators=250)
forest.fit(X, Y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],axis=0)
indices = np.argsort(importances)[::-1]

# indices=[ 0,2,3,4,5,7,8,9,14,23,32,36,38,39,40]
from random import shuffle
shuffle(indices)

#https://www.kaggle.com/willkoehrsen/visualize-a-decision-tree-w-python-scikit-learn

# from sklearn.ensemble import RandomForestClassifier
# temp = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
# temp.fit(X,Y)
# estimator = temp.estimators_[5]

# from sklearn.tree import export_graphviz
# export_graphviz(estimator, out_file='tree.dot', 
                # feature_names = Features,
                # class_names = ["Baiat","Femeie"],
                # rounded = True, proportion = False, 
                # filled = True)
# from subprocess import call
# call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
# import matplotlib.pyplot as plt
# plt.figure(figsize = (14, 18))
# plt.imshow(plt.imread('tree.png'))
# plt.axis('off');
# plt.show();



X=normalize(X)

#https://markhneedham.com/blog/2013/11/06/python-generate-all-combinations-of-a-list/
# import itertools as it
# Index=list(range(0,len(Features)))
# all_the_features = []
# for r in range(1, len(Index) + 1):
	# all_the_features +=list(it.combinations(Index, r))


results = []
names = []
Subfeatures = []
mods = []
for i in range(1,len(indices)):
# for i in range( round(len(indices)/4),round(len(indices)/3) ):
	for name, model in models:
		#https://stackoverflow.com/questions/8386675/extracting-specific-columns-in-numpy-array
		subset=indices[0:i]
		XTemp=X[:,subset]
		kfold = model_selection.StratifiedKFold(n_splits=10, shuffle=True)
		cv_results = model_selection.cross_val_score(model, XTemp, Y, cv=kfold, scoring='accuracy')
		
		results.append(cv_results)
		names.append(name)
		Subfeatures.append(subset)
		mods.append(model)
		
		msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
		ma=cv_results.mean()
		print(subset,msg)
			

#index of best n results :  https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
BestIndex=np.array([x.mean() for x in results]).argsort()[::-1][:10]
results=np.array(results)[BestIndex]
names=np.array(names)[BestIndex]
Subfeatures=np.array(Subfeatures)[BestIndex]
mods=np.array(mods)[BestIndex]



#https://datascience.stackexchange.com/questions/37899/sklearn-svm-how-to-get-a-list-of-the-wrong-predictions
inds = np.arange(Y.shape[0])
X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(X, Y, inds, stratify=Y, test_size=0.2)
BestModel=mods[0]
BestModel.fit(X_train, y_train)
BestPredict = BestModel.predict(X_test)


#Var2
#https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
# from statistics import mode
from collections import Counter

for mod in mods:
	mod.fit(X_train, y_train)
for input, prediction,index in zip (inds[idx_test], BestPredict,inds):
	BestPredict[index] = Counter([  mod.predict( np.array(X[input]).reshape(1,-1) )[0]  for mod in mods ]).most_common(1)[0][0]



for input, prediction, label in zip (inds[idx_test], BestPredict, y_test):
	if prediction != label:
		#https://i.kym-cdn.com/photos/images/newsfeed/001/191/035/135.png
		print(input+1, ' classified as ', prediction, ' is achsiualy ', label, end =" -> ")
		print(BestModel.predict_proba( np.array(X[input]).reshape(1,-1)    ) )
		
		#https://stackoverflow.com/questions/35082140/preprocessing-in-scikit-learn-single-sample-depreciation-warning


print( (BestPredict==y_test).mean()  ,results[0].mean())
print(names[0],Subfeatures[0])
	
from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(y_test,BestPredict ).ravel()
print (tn, fp, fn, tp)

# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results.tolist())
ax.set_xticklabels(names)
plt.show()

