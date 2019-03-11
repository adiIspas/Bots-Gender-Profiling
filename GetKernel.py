import re
from collections import Counter
import reader as reader
import numpy as np
import time
import datetime
Dir='PAN\\en\\';
# linesTrain = open(Dir+'truth-train.txt').read().splitlines()
linesTrain = open(Dir+'truth.txt').read().splitlines()
start_time = time.time()




def XML2Pgrams(file,pgram=2):
	tweets=reader.get_tweets(file)
	oneLongTweet=' '.join(tweets)
	oneLongTweet = oneLongTweet.lower()
	oneLongTweet = re.sub(r'^https:\/\/.*[\r\n]*', 'secure', oneLongTweet)
	oneLongTweet = re.sub(r'^http:\/\/.*[\r\n]*', 'unsecure', oneLongTweet)
	oneLongTweet=' '.join(oneLongTweet.split())
	return Counter([oneLongTweet[i:i + pgram] for i in range(0, len(oneLongTweet )-pgram +1 )])
	

# pine= Counter(['pineapple'[i:i + 2] for i in range(0, len('pineapple') -2 + 1)])
# apple= Counter(['apple pie'[i:i + 2] for i in range(0, len('apple pie') -2 +1)])
	
	
# def KernelFrom2Lists(A,B,type):
	# ret=0
	# for pair in set(list(A.keys())+list(B.keys())):
		# if(type=='Intersection'):
			# ret+=min(A[pair],B[pair])
		# if(type=='Presence'):
			# ret+= 1 if A[pair]*B[pair] !=0 else 0
		# if(type=='Spectrum'):
			# ret+=A[pair]*B[pair]
	# return ret
def KernelFrom2ListsIntersect(A,B):
	ret=0
	for pair in A.keys():
		ret+=min(A[pair],B[pair])
	return ret
	

X_Train=np.empty([len(linesTrain),len(linesTrain)], dtype=int)
Y_Train=np.empty([len(linesTrain), ],dtype=int)
	
Cache=np.empty([len(linesTrain), ],dtype=object)
for i in range(len(linesTrain)):
	tokens=linesTrain[i].split(':::')
	Cache[i]=XML2Pgrams(Dir+tokens[0]+'.xml')
	Y_Train[i]=['bot','male','female'].index(tokens[2])
	
print('--- Cached:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))

for i in range(len(linesTrain)):
	print(100.0*i/len(linesTrain))
	for j in range(i,len(linesTrain)):
		X_Train[i][j]=KernelFrom2ListsIntersect(Cache[i],Cache[j])
		X_Train[j][i]=X_Train[i][j]
		

print('--- Total time of execution:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))


#todo:
#export to txt sa comparam cu ala a lu marius
fout= open("da.txt","w")
for i in range(len(linesTrain)):
	for j in range(len(linesTrain)):
		fout.write("%d " % X_Train[i][j])
	fout.write('\n')
#normalizare