import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.feature_selection import VarianceThreshold
import datetime
print(datetime.datetime.now())

f = open("x_features.txt")
# f = open("C:\\Users\\One\\Desktop\\pan19-author-profiling-training-2019-02-18\\en\\x_features.txt")
# f = open("F:\\Personal\\bricks\\mabri\\dateleu.out")
# f = open("C:\\Users\\One\\Desktop\\mean\\1-20.out")
Features=f.readline().split(',')
Features.pop(0)#Primu e clasa


data = np.loadtxt(f,delimiter=",")
Y=data[:,0]
X=data[:,1:]


BestOfAll=np.full(len(Features),True,dtype=bool)

print("\n\nVariance")
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)
print(sel.get_support())
BestOfAll=np.logical_and(BestOfAll,sel.get_support())
for idx, val in enumerate(sel.get_support()):
	if(val):
		print(Features[idx])
		
		
		
print("\n\nChi2")
from sklearn.feature_selection import SelectKBest,chi2
sel = SelectKBest(chi2, k= round(len(Features)/2))
sel.fit_transform(X,Y)
print(sel.get_support())
BestOfAll=np.logical_and(BestOfAll,sel.get_support())
for idx, val in enumerate(sel.get_support()):
	if(val):
		print(Features[idx])		
		
print("\n\nf_classif")
from sklearn.feature_selection import f_classif
sel = SelectKBest(f_classif, k= round(len(Features)/2))
sel.fit_transform(X,Y)
print(sel.get_support())
BestOfAll=np.logical_and(BestOfAll,sel.get_support())
for idx, val in enumerate(sel.get_support()):
	if(val):
		print(Features[idx])
		
		
		

print("\n\ncele mai importante 50%")
from sklearn.feature_selection import SelectPercentile
sel=SelectPercentile(f_classif, percentile=50)
sel.fit_transform(X, Y)
print(sel.get_support())
BestOfAll=np.logical_and(BestOfAll,sel.get_support())
for idx, val in enumerate(sel.get_support()):
	if(val):
		print(Features[idx])

print("\n\nBestOfAll")
for idx, val in enumerate(BestOfAll):
	if(val):
		print(Features[idx])
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_and.html
#https://scikit-learn.org/stable/modules/feature_selection.html
#https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops