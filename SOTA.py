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


from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC



from sklearn.tree import ExtraTreeClassifier
from sklearn.multiclass import OutputCodeClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model.stochastic_gradient import SGDClassifier
from sklearn.linear_model.ridge import RidgeClassifierCV
from sklearn.linear_model.ridge import RidgeClassifier
from sklearn.linear_model.passive_aggressive import PassiveAggressiveClassifier    
from sklearn.gaussian_process.gpc import GaussianProcessClassifier
from sklearn.ensemble.voting_classifier import VotingClassifier
from sklearn.ensemble.bagging import BaggingClassifier
from sklearn.ensemble.forest import ExtraTreesClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.calibration import CalibratedClassifierCV
from sklearn.semi_supervised import LabelPropagation
from sklearn.semi_supervised import LabelSpreading
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegressionCV
from sklearn.naive_bayes import MultinomialNB  
from sklearn.neighbors import NearestCentroid
from sklearn.linear_model import Perceptron
from sklearn.mixture import DPGMM
from sklearn.mixture import GMM 
from sklearn.mixture import GaussianMixture
from sklearn.mixture import VBGMM



#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
#todo, sa vad vecinii aia naspa


# f = open("es_train_data.csv")
f = open("en_train_data.csv")
Features=f.readline().split(',')#It gives head
data = np.loadtxt(f,delimiter=",")
Features.pop(-1)#ultimu e clasa
X_Train=data[:, :-1]
Y_Train=data[:,-1]



# f = open("es_dev_data.csv")
f = open("en_dev_data.csv")
Features=f.readline().split(',')#It gives head
data = np.loadtxt(f,delimiter=",")
Features.pop(-1)#ultimu e clasa
X_Test=data[:, :-1]
Y_Test=data[:,-1]



models = []
models.append(('LR1', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('Knn1',     KNeighborsClassifier(1) ))
models.append(('Knn9D',     KNeighborsClassifier(9, weights='distance') ))
models.append(('LSVM',     SVC(kernel="linear")  ))
models.append(('RBF',     SVC()  ))
models.append(('DT',     DecisionTreeClassifier(max_depth=5) ))
models.append(('RF',     RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1) ))
models.append(('NN1',     MLPClassifier(alpha=0.1) ))
models.append(('AB',     AdaBoostClassifier() ))
models.append(('NB',     GaussianNB() ))
models.append(('QDA',     QuadraticDiscriminantAnalysis()  ))
models.append(('NuSVC',     NuSVC(probability=True)  ))
models.append(('GBC',     GradientBoostingClassifier()  ))
models.append(('Q2',     BaggingClassifier()  ))


models.append(('RBF2',     SVC(kernel="rbf", C=0.025, probability=True)  ))
models.append(('ETC',     ExtraTreeClassifier()  ))
models.append(('Q1',     SGDClassifier()  ))
models.append(('Q2',     RidgeClassifier()  ))
models.append(('Q2',     PassiveAggressiveClassifier()  ))
# models.append(('Q2',     GaussianProcessClassifier()  ))
models.append(('Q3',     ExtraTreesClassifier()  ))
models.append(('Q3',     BernoulliNB()  ))
models.append(('Q3',     GaussianMixture()  ))
# models.append(('Q4',     GMM()  ))


Medii=[]
for name, model in models:
	model.fit(X_Train,Y_Train)
	Medii.append((model.predict(X_Test)==Y_Test).mean())
	
Mean=np.array(Medii).mean()
models = [x for ind, x in enumerate(models) if Medii[ind]>Mean]




# #B/H
# Y_Train_BH=[1 if y>0 else 0 for y in Y_Train]
# Y_Test_BH=[1 if y>0 else 0 for y in Y_Test]

# #M/F
# Y_Train_MF=Y_Train[round(0.5*len(Y_Train)):]
# X_Train_MF=X_Train[round(0.5*len(X_Train)):,:]
# Y_Test_MF=Y_Test[round(0.5*len(Y_Test)):]
# X_Test_MF=X_Test[round(0.5*len(X_Test)):,:]


#AB LR sau NN NN



	


# X_Train=normalize(X_Train)
# X_Test=normalize(X_Test)

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
import random
# shuffle(indices)


from collections import Counter
def Most(List):
	return Counter(List).most_common(1)[0][0]

	
	
	
	

fout= open("KaEnEn.txt","w")

results = []
names = []
Subfeatures = []

Preds =[]
if True:
# for i in range(1,len(indices)):
# for i in range(32,33):
	# subset=indices[0:i]
	for name, model in models:
	
	
		#Partea de B vs H
		# XTempTrain=X_Train[:,subset]
		# XTempTest=X_Test[:,subset]
		
		model.fit(X_Train,Y_Train)
		Pred=model.predict(X_Test)
		
		for j in range(len(Pred)):
			fout.write("%d" % Pred[j])
		fout.write('\n')
		
		Preds.append( Pred )
		# acc=np.array(Pred==Y_Test).mean()
		# results.append( acc )
		# names.append(nameBH+' si '+nameMF)
		# Subfeatures.append(subset)
		
		# print(subset,nameBH+' si '+nameMF,' acc1: ',acc1, ' acc2: ',acc2,' acc: ',acc)

# ma=0
# WV=VotingClassifier(models)
# WV.fit(X_Train,Y_Train)
# for i in range(1000):
	# Ran=np.random.dirichlet(np.ones(len(models)))
	# WV.set_params(weights=Ran)
	# Pred=WV.predict(X_Test)
	# acc=(Pred==Y_Test).mean()
	# if acc>ma:
		# ma=acc
		# print(Ran)
		# print(acc)
		# print('\n')


	
	
WV=VotingClassifier(models)
WV.fit(X_Train,Y_Train)
Pred=WV.predict(X_Test)
print((Pred==Y_Test).mean())



for j in range(len(Pred)):
	fout.write("%d" % Pred[j])
fout.write('\n')
for j in range(len(Y_Test)):
	fout.write("%d" % Y_Test[j])
fout.write('\n')
			
fout.close()
exit(0)
			

#index of best n results :  https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
BestIndex=np.array([x for x in results]).argsort()[::-1][:10]
results=np.array(results)[BestIndex]
names=np.array(names)[BestIndex]
Subfeatures=np.array(Subfeatures)[BestIndex]

for i in range(10):
	print("ACC: ",results[i],' name: ',names[i], 'sub: ',Subfeatures[i])
