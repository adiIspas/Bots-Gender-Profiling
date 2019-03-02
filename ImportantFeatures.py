import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.feature_selection import VarianceThreshold
import datetime
print(datetime.datetime.now())

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
		
		
# nu ii plac valori negative :(	
# print("\n\nChi2")
# from sklearn.feature_selection import SelectKBest,chi2
# sel = SelectKBest(chi2, k= round(len(Features)/2))
# sel.fit_transform(X,Y)
# print(sel.get_support())
# BestOfAll=np.logical_and(BestOfAll,sel.get_support())
# for idx, val in enumerate(sel.get_support()):
	# if(val):
		# print(Features[idx])		
		
print("\n\nf_classif")
from sklearn.feature_selection import SelectKBest,f_classif
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