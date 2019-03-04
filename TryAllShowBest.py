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

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('Knn3',     KNeighborsClassifier(3) ))
models.append(('Knn5',     KNeighborsClassifier(5) ))
models.append(('LSVM',     SVC(kernel="linear")  ))
models.append(('RBF',     SVC()  ))
models.append(('DT',     DecisionTreeClassifier(max_depth=5) ))
models.append(('RF',     RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1) ))
models.append(('NN',     MLPClassifier(alpha=1) ))
models.append(('AB',     AdaBoostClassifier() ))
models.append(('NB',     GaussianNB() ))
models.append(('QDA',     QuadraticDiscriminantAnalysis()  ))





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



#https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html
from sklearn.ensemble import ExtraTreesClassifier
forest = ExtraTreesClassifier(n_estimators=250,random_state=0)
forest.fit(X, Y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],axis=0)
indices = np.argsort(importances)[::-1]


# X=normalize(X)

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
# for i in range(1,len(Features)):
for i in range( round(len(Features)/4),round(len(Features)/3) ):
	for name, model in models:
		#https://stackoverflow.com/questions/8386675/extracting-specific-columns-in-numpy-array
		subset=indices[0:i]
		XTemp=X[:,subset]
		kfold = model_selection.StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
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





#https://datascience.stackexchange.com/questions/37899/sklearn-svm-how-to-get-a-list-of-the-wrong-predictions
inds = np.arange(Y.shape[0])
X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(X, Y, inds, stratify=Y, test_size=0.2,
                                                                         random_state=42)
model_0=np.array(mods)[0]
model_1=np.array(mods)[1]
model_2=np.array(mods)[2]
classifier_0=model_0.fit(X_train, y_train)
classifier_1=model_1.fit(X_train, y_train)
classifier_2=model_2.fit(X_train, y_train)
predictions_0 = model_0.predict(X_test)
predictions_1 = model_1.predict(X_test)
predictions_2 = model_2.predict(X_test)



for input, p0,p1,p2, label in zip (inds[idx_test], predictions_0,predictions_1,predictions_2, y_test):
  prediction = round((p0+p1+p2)/3.0)
  if prediction != label:
    print(input+1, 'has been classified as ', prediction, 'and should be ', label)

preds=(predictions_0+predictions_1+predictions_2)
print( (predictions_0==y_test).mean()  )
print( (predictions_1==y_test).mean()  )
print( (predictions_2==y_test).mean()  )
print( (([round(x/3.0) for x in preds])==y_test).mean() )
	
from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(y_test,([round(x/3.0) for x in preds]) ).ravel()
print (tn, fp, fn, tp)

# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results.tolist())
ax.set_xticklabels(names)
plt.show()


