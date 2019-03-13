from sklearn.svm import SVC
from sklearn.svm import NuSVC
import numpy as np
import re
from collections import Counter
import reader as reader
import numpy as np
import time
import datetime
Dir='PAN/en/';

linesTest = open(Dir+'truth-dev.txt').read().splitlines()
linesTrain = open(Dir+'truth-train.txt').read().splitlines()

start_time = time.time()

K=np.loadtxt('Kernel2.txt')
N_Train=len(linesTrain)
N_Test=len(linesTest)
N=N_Train+N_Test

Y=np.empty([N, ],dtype=int)
i=0
for line in linesTrain+linesTest:
	tokens=line.split(':::')
	Y[i]=['bot','male','female'].index(tokens[2])
	i=i+1

nu=0.5
for _ in range(10):
	clf = NuSVC(nu,kernel='precomputed', )#,#verbose =True,      shrinking=False,
	clf.fit(K[0:N_Train,0:N_Train], Y[0:N_Train])
	AccTrain=(clf.predict(K[0:N_Train,0:N_Train])==Y[0:N_Train]).mean()
	AccTest=(clf.predict(K[N_Train:,0:N_Train])==Y[N_Train:]).mean()
	print('nu= ',nu,' acc pe train: ' ,AccTrain,' Acc pe test: ',AccTest)
	nu*=0.95














