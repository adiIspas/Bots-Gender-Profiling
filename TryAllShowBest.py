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
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
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
models.append(('LSVM',     SVC(kernel="linear")  ))
models.append(('RBF',     SVC()  ))
models.append(('DT',     DecisionTreeClassifier(max_depth=5) ))
models.append(('RF',     RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1) ))
models.append(('NN1',     MLPClassifier(alpha=0.1) ))
models.append(('AB',     AdaBoostClassifier() ))
models.append(('NB',     GaussianNB() ))
models.append(('QDA',     QuadraticDiscriminantAnalysis()  ))


#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
#todo, sa vad vecinii aia naspa


f = open("en_train_data.csv")
Features=f.readline().split(',')#It gives head
data = np.loadtxt(f,delimiter=",")
Features.pop(-1)#ultimu e clasa
Y_Train=data[:,-1]
X_Train=data[:, :-1]



f = open("en_dev_data.csv")
Features=f.readline().split(',')#It gives head
data = np.loadtxt(f,delimiter=",")
Features.pop(-1)#ultimu e clasa
Y_Test=data[:,-1]
X_Test=data[:, :-1]


#B/H
# Y_Train=[1 if y>0 else 0 for y in Y_Train]
# Y_Test=[1 if y>0 else 0 for y in Y_Test]

#M/F
# Y_Train[round(0.5*len(Y_Train)):]
# X_Train[round(0.5*len(X_Train)):,:]
# Y_Test[round(0.5*len(Y_Test)):]
# X_Test[round(0.5*len(X_Test)):,:]






#Normalizare 1
# X_Train=normalize(X_Train)
# X_Test=normalize(X_Test)




#Normalizare 2
# m=len(Features)
# mins=[ min(X_Train[:,col].min(),X_Test[:,col].min()) for col in range(m)]
# maxs=[ max(X_Train[:,col].max(),X_Test[:,col].max()) for col in range(m)]

# for j in range(m):
	# X_Train[:,j]=(X_Train[:,j]-mins[j])/(maxs[j]-mins[j]+1)
	# X_Test[:,j]=(X_Test[:,j]-mins[j])/(maxs[j]-mins[j]+1)
		
		
		


#https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html
from sklearn.ensemble import ExtraTreesClassifier
forest = ExtraTreesClassifier(n_estimators=250)
forest.fit(X_Train, Y_Train)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],axis=0)
indices = np.argsort(importances)[::-1]

# indices=[ 0,2,3,4,5,7,8,9,14,23,32,36,38,39,40]
from random import shuffle
# shuffle(indices)




results = []
names = []
Subfeatures = []
mods = []
for i in range(1,len(indices)):
# for i in range( round(len(indices)/4),round(len(indices)/3) ):
	for name, model in models:
		#https://stackoverflow.com/questions/8386675/extracting-specific-columns-in-numpy-array
		subset=indices[0:i]
		XTemp=X_Train[:,subset]
		XTempTest=X_Test[:,subset]
		
		model.fit(XTemp,Y_Train)
		# kfold = model_selection.StratifiedKFold(n_splits=10, shuffle=True)
		# cv_results = model_selection.cross_val_score(model, XTemp, Y, cv=kfold, scoring='accuracy')
		
		acc=np.array(model.predict(XTempTest)==Y_Test).mean()
		
		results.append( acc )
		names.append(name)
		Subfeatures.append(subset)
		mods.append(model)
		
		# msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
		# ma=cv_results.mean()
		print(subset,name,acc)
			

#index of best n results :  https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
BestIndex=np.array([x for x in results]).argsort()[::-1][:10]
results=np.array(results)[BestIndex]
names=np.array(names)[BestIndex]
Subfeatures=np.array(Subfeatures)[BestIndex]
mods=np.array(mods)[BestIndex]

for i in range(10):
	print("ACC: ",results[i],' name: ',names[i])
