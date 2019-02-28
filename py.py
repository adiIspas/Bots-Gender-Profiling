import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

from sklearn.feature_selection import VarianceThreshold
import datetime
print(datetime.datetime.now())

f = open("C:\\Users\\One\\Desktop\\pan19-author-profiling-training-2019-02-18\\en\\x_features.txt")
# f = open("F:\\Personal\\bricks\\mabri\\dateleu.out")
# f = open("C:\\Users\\One\\Desktop\\mean\\1-20.out")
data = np.loadtxt(f,delimiter=",")

target=data[:,0]
features=data[:,1:]


# print(features.shape)
# from sklearn.feature_selection import SelectPercentile, chi2,f_classif
# sel=SelectPercentile(f_classif, percentile=50)
# features = sel.fit_transform(features, target)
# print(sel.get_support())
# print(features.shape)



X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

X_train.shape, y_train.shape
X_test.shape, y_test.shape

clf = svm.SVC(kernel='rbf', C=1,verbose=1,shrinking=False,cache_size=1000).fit(X_train, y_train)
# clf = svm.SVC(kernel='linear', C=1,verbose=1,shrinking=False,cache_size=1000).fit(X_train, y_train)
print(clf.score(X_test, y_test))
print("\n")
print(datetime.datetime.now())