import re
import time
import datetime
from collections import Counter
import reader as reader
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer(preserve_case=False)

from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
ps = PorterStemmer() 


Dir='PAN\\en\\';
# fout= open(Dir+"x_features.txt","w")
# lines = open(Dir+'truth-train.txt').read().splitlines()


N_WORDS=128


# ret=Counter()
# def GetWords(file):
	# rety=Counter()
	# tweets=reader.get_tweets(file)
	# for tweet in tweets:
		# words=tknzr.tokenize(tweet)
		# words= [ps.stem(w) for w in words]
		# for w in words:
			# rety[w]+=1
	# return rety
	



# for idx,line in enumerate(lines):
	# tokens=line.split(':::')
	# ret+=GetWords(Dir+tokens[0]+'.xml')
	# if idx%50==0:
		# print(100.0*idx/len(lines))
	
# Top1000Words=[k for (k,v) in ret.most_common(N_WORDS)]


start_time = time.time()


print('--- Total time of execution:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))














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
from sklearn.preprocessing import scale

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
# models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('Knn1',     KNeighborsClassifier(1) ))
models.append(('Knn3',     KNeighborsClassifier(3) ))
models.append(('Knn5',     KNeighborsClassifier(5) ))
models.append(('Knn1D',     KNeighborsClassifier(1, weights='distance') ))
models.append(('Knn3D',     KNeighborsClassifier(3, weights='distance') ))
models.append(('Knn5D',     KNeighborsClassifier(5, weights='distance') ))
# models.append(('Knn7D',     KNeighborsClassifier(7, weights='distance') ))
# models.append(('Knn9D',     KNeighborsClassifier(9, weights='distance') ))
# models.append(('Knn11D',     KNeighborsClassifier(11, weights='distance') ))
# models.append(('Knn13D',     KNeighborsClassifier(13, weights='distance') ))
#models.append(('LSVM',     SVC(kernel="linear")  ))
# models.append(('RBF',     SVC()  ))
models.append(('DT',     DecisionTreeClassifier(max_depth=5) ))
models.append(('RF',     RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1) ))
models.append(('NN',     MLPClassifier(alpha=1) ))
models.append(('AB',     AdaBoostClassifier() ))
# models.append(('NB',     GaussianNB() ))
# models.append(('QDA',     QuadraticDiscriminantAnalysis()  ))





#truth-train.txt
#truth-dev.txt
linesTrain = open(Dir+'truth-train.txt').read().splitlines()
linesTest = open(Dir+'truth-dev.txt').read().splitlines()


X_Train=np.empty([len(linesTrain)*100, N_WORDS+1], dtype=float)
Y_Train=np.empty([len(linesTrain)*100, ],dtype=float)

X_Test=np.empty([len(linesTest)*100, N_WORDS+1], dtype=float)
Y_Test=np.empty([len(linesTest)*100, ],dtype=float)


for idx,line in enumerate(linesTrain):
	tokens=line.split(':::')
	tweets=reader.get_tweets(Dir+tokens[0]+'.xml')
	for idy,tweet in enumerate(tweets):
		p=idx*100+idy
		Y_Train[p]=['bot','male','female'].index(tokens[2])
		if(Y_Train[p]==2):
			Y_Train[p]=1
		for l in tweet:
			o=ord(l)
			if(o<N_WORDS):
				X_Train[p][o]+=1
			if(o>=N_WORDS):
				X_Train[p][N_WORDS]+=1
	
	
for idx,line in enumerate(linesTest):
	tokens=line.split(':::')
	tweets=reader.get_tweets(Dir+tokens[0]+'.xml')
	for idy,tweet in enumerate(tweets):
		p=idx*100+idy
		Y_Test[p]=['bot','male','female'].index(tokens[2])
		if(Y_Test[p]==2):
			Y_Test[p]=1
		for l in tweet:
			o=ord(l)
			if(o<N_WORDS):
				X_Test[p][o]+=1
			if(o>=N_WORDS):
				X_Test[p][N_WORDS]+=1
	
	
	
	
	
# for idx,line in enumerate(linesTrain):
	# tokens=line.split(':::')
	# Words=GetWords(Dir+tokens[0]+'.xml')
	# nrWords=sum(Words.values())
	# nrKnownWords=0
	# Y_Train[idx]=['bot','male','female'].index(tokens[2])
	# if idx%50==0:
		# print(100.0*idx/len(linesTrain))
	# for x,w in enumerate(Top1000Words):
		# nrKnownWords+=Words[w]
		# X_Train[idx][x]=Words[w]/(1+nrWords)
	# X_Train[idx][-1]=(nrWords-nrKnownWords)/(1+nrWords)

# for idx,line in enumerate(linesTest):
	# tokens=line.split(':::')
	# Words=GetWords(Dir+tokens[0]+'.xml')
	# nrWords=sum(Words.values())
	# nrKnownWords=0
	# Y_Test[idx]=['bot','male','female'].index(tokens[2])
	# if idx%50==0:
		# print(100.0*idx/len(linesTest))
	# for x,w in enumerate(Top1000Words):
		# nrKnownWords+=Words[w]
		# X_Test[idx][x]=Words[w]/(1+nrWords)
	# X_Test[idx][-1]=(nrWords-nrKnownWords)/(1+nrWords)
	


	
#tre testate 3 feluri de normalizare: fara, pe linie, pe col
# X_Train=normalize(X_Train)
# X_Test=normalize(X_Test)

# X_Train=normalize(X_Train,axis =0)
# X_Test=normalize(X_Test,axis=0)
# X_Train=scale(X_Train )
# X_Test=scale(X_Test)

# scaler = StandardScaler()

# for name, model in models:
	# kfold = model_selection.StratifiedKFold(n_splits=10, shuffle=True)
	# cv_results = model_selection.cross_val_score(model, X_Train, Y_Train, cv=kfold, scoring='accuracy')
	
	# results.append(cv_results)
	# names.append(name+"Norm")
	# mods.append(model)
	
	# msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	# ma=cv_results.mean()
	# print(msg)
			

# X_Train=normalize(X_Train)
# X_Test=normalize(X_Test)
#index of best n results :  https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
for name, model in models:
	model.fit(X_Train, Y_Train)
	BestPredict = model.predict(X_Test)
	print( (BestPredict==Y_Test).mean(), ' ',name )
	

	
	
print('--- Total time of execution:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))