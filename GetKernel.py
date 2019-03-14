import signal
#cel mai important import

import re
from collections import Counter
import reader as reader
import numpy as np
import time
import datetime
Dir='PAN\\en\\';

linesTest = open(Dir+'truth-dev.txt').read().splitlines()
linesTrain = open(Dir+'truth-train.txt').read().splitlines()
start_time = time.time()

FILENAME="Kernel2I.txt"


def XML2Pgrams(file,pgram=2):
	tweets=reader.get_tweets(file)
	oneLongTweet=' '.join(tweets)
	oneLongTweet = oneLongTweet.lower()
	oneLongTweet = re.sub(r'^https:\/\/.*[\r\n]*', 'secure', oneLongTweet)
	oneLongTweet = re.sub(r'^http:\/\/.*[\r\n]*', 'unsecure', oneLongTweet)
	oneLongTweet=' '.join(oneLongTweet.split())
	return Counter([oneLongTweet[i:i + pgram] for i in range(0, len(oneLongTweet )-pgram +1 )])
	
def XML2PgramsWords(file,pgram=5):
	tweets=reader.get_tweets(file)
	oneLongTweet=' '.join(tweets)
	oneLongTweet = oneLongTweet.lower()
	oneLongTweet = re.sub(r'^https:\/\/.*[\r\n]*', 'secure', oneLongTweet)
	oneLongTweet = re.sub(r'^http:\/\/.*[\r\n]*', 'unsecure', oneLongTweet)
	oneLongTweet=oneLongTweet.split()
	return Counter([  ' '.join(oneLongTweet[i:i + pgram]) for i in range(0, len(oneLongTweet )-pgram +1 )])
		
def XML2Fetures(file):
	return [XML2PgramsWords(file,i).most_common(1)[0][1]   for i in [5,10,15,20]]
		

# pine= Counter(['pineapple'[i:i + 2] for i in range(0, len('pineapple') -2 + 1)])
# apple= Counter(['apple pie'[i:i + 2] for i in range(0, len('apple pie') -2 +1)])
	
	
def KernelFrom2ListsIntersect(A,B):
	ret=0
	if(len(A)<len(B)):
		for pair in A.keys():
			a=A[pair]
			b=B[pair]
			if(a<b):
				ret+=a
			else:
				ret+=b
			# ret+=min(A[pair],B[pair])
	else:
		for pair in B.keys():
			a=A[pair]
			b=B[pair]
			if(a<b):
				ret+=a
			else:
				ret+=b
	return ret
def KernelFrom2ListsSpectrum(A,B):
	ret=0
	if(len(A)<len(B)):
		for pair in A.keys():
			ret+=A[pair]*B[pair]
	else:
		for pair in B.keys():
			ret+=A[pair]*B[pair]
	return ret
def KernelFrom2ListsPresence(A,B):
	ret=0
	if(len(A)<len(B)):
		for pair in A.keys():
			if(B[pair]!=0):
				ret+=1
	else:
		for pair in B.keys():
			if(B[pair]!=0):
				ret+=1
	return ret
	
N_Train=len(linesTrain)
N_Test=len(linesTest)
N=N_Train+N_Test

Kernel=np.empty([N,N], dtype=float)
Cache=np.empty([N, ],dtype=object)


i=0
for line in linesTrain+linesTest:
	tokens=line.split(':::')
	Cache[i]=XML2Pgrams(Dir+tokens[0]+'.xml')
	i=i+1
	
print('--- Cached:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))




#<SEPARAT>
fisier=Dir+(linesTrain[0].split(':::'))[0]+'.xml'
for p in range(2,50):
	temp=XML2Pgrams(fisier,p)
	
	
	start_time = time.time()
	for i in range(100):
		KernelFrom2ListsIntersect(temp,temp)
	print('p: ',p,' KernelFrom2ListsIntersect %s' % (datetime.timedelta(seconds=40000*(time.time() - start_time))   ))
	
	
	start_time = time.time()
	for i in range(100):
		KernelFrom2ListsSpectrum(temp,temp)
	print('p: ',p,' KernelFrom2ListsSpectrum %s' % (datetime.timedelta(seconds=40000*(time.time() - start_time))   ))
	
	
	start_time = time.time()
	for i in range(100):
		KernelFrom2ListsPresence(temp,temp)
	print('p: ',p,' KernelFrom2ListsPresence %s' % (datetime.timedelta(seconds=40000*(time.time() - start_time))   ))
	print('\n')

#</SEPARAT>
	
	
	
	
for i in range(N):
	print(100.0*i/N)
	print('--- Cached:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))
	for j in range(i,N):
		Kernel[i][j]=KernelFrom2ListsIntersect(Cache[i],Cache[j])
		Kernel[j][i]=Kernel[i][j]

		

print('--- Total time of execution:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))
	
#normalizare
from math import sqrt
for i in range(N):
	for j in range(N):
		if(i!=j):
			Kernel[i][j]/=sqrt(Kernel[i][i]*Kernel[j][j]+1)

for i in range(N):
	Kernel[i][i]=1
	

	
#export to txt sa comparam cu ala a lu marius
fout= open(FILENAME,"w")
for i in range(N):
	for j in range(N):
		fout.write("%1.4f " % Kernel[i][j])
	fout.write('\n')

fout.close()