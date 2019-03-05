import re
from collections import Counter

Dir='PAN\\en\\';
fout= open(Dir+"x_features.txt","w")
lines = open(Dir+'truth-train.txt').read().splitlines()

fout.write("Clasa,Diez,At,Link,Percent,NrVirgula,NrPct,NrNr,NrExclamare,NrIntrebare,he,she  ,NrLinii,LungimeMedie\n")

strBot=""
strOm =""

strF=""
strM=""
for line in lines:
	tokens=line.split(':::')
	fil=open(Dir+tokens[0]+'.xml', encoding="utf8").read().splitlines()
	
	if(True):
		if(tokens[2]=="bot"):
			fout.write("0, ")
			strBot+=" ".join(fil)
		if(tokens[2]=="male"):
			fout.write("1, ")
			strM+=" ".join(fil)
		if(tokens[2]=="female"):
			fout.write("2, ")
			strF+=" ".join(fil)
		
		L=[len(x) for x in fil]
		Length=sum(L) / float(len(L));
		# fout.write("%d, " % sum([ ("#" in x) for x in fil]))
		# fout.write("%d, " % sum([ ("@" in x) for x in fil]))
		# fout.write("%d, " % sum([ ("http" in x) for x in fil]))
		# fout.write("%d, " % sum([ ("%" in x) for x in fil]))
		# fout.write("%d, " % sum([ ("," in x) for x in fil]))
		# fout.write("%d, " % sum([ ("." in x) for x in fil]))
		fout.write("%d, " % sum([ x.count("#") for x in fil]))
		fout.write("%d, " % sum([ x.count("@") for x in fil]))
		fout.write("%d, " % sum([ x.count("http") for x in fil]))
		fout.write("%d, " % sum([ x.count("%") for x in fil]))
		fout.write("%d, " % sum([ x.count(",") for x in fil]))
		fout.write("%d, " % sum([ x.count(".") for x in fil]))
		fout.write("%d, " % sum([ sum(c.isdigit() for c in x) for x in fil]))
		fout.write("%d, " % sum([ x.count("!") for x in fil]))
		fout.write("%d, " % sum([ x.count(" he ")+x.count(" his ")+x.count(" man ")+x.count(" boy ") for x in fil]))
		fout.write("%d, " % sum([ x.count(" she ")+x.count(" her ")+x.count(" woman ")+x.count(" girl ") for x in fil]))
		
		fout.write("%d, " % len(fil))
		fout.write("%d\n" % Length)

		

strOm=strF+" "+strM
strF=strF.lower()
strM=strM.lower()

strBot=strBot.lower()
strOm=strOm.lower()


str_listF=re.findall(r"[\w']+", strF)
str_listM=re.findall(r"[\w']+", strM)

str_listBot=re.findall(r"[\w']+", strBot)
str_listOm=re.findall(r"[\w']+", strOm)



#Daca faci asta e si bine, e si rau:
#E bine ca pui la un loc game, games si astfel au importanta mai mare si gasesti mai multe cuvinte diferite/utile (gen nu era la baieti "cunt" fara stemming)
#Dar e rau ca dispar subtilitati (femeile trimit mai multe https decat baietii care trimit http mai mult, cel mai probabil fetele trimit linkuri gen fb, yt, instagram care sunt cu s la sfarsit, baietii trimit chestii mai diverse)
#Dar e bine ca vezi ca fetele trimit mai multe linkuri decat baietii

#nu e chiar hardcodeala ca apar chestii la care ne asteptam, la baieti fuck e in primele 10, cunt in primele 100
#la fete: love, life, happy, instagram primele 100

from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
ps = PorterStemmer() 
str_listF= [ps.stem(w) for w in str_listF]
str_listM= [ps.stem(w) for w in str_listM]
str_listBot= [ps.stem(w) for w in str_listBot]
str_listOm= [ps.stem(w) for w in str_listOm]





f=Counter(str_listF)
m=Counter(str_listM)

bot=Counter(str_listBot)
om=Counter(str_listOm)

for k in f.keys():
	f[k]=f[k]/len(str_listF)
	
for k in m.keys():
	m[k]=m[k]/len(str_listM)

for k in bot.keys():
	bot[k]=bot[k]/len(str_listBot)
	
for k in om.keys():
	om[k]=om[k]/len(str_listOm)
	
f.subtract(m)
om.subtract(bot)
#Varianta 1: facem diferenta pe countere
#https://docs.python.org/2/library/collections.html#collections.Counter         Dif.most_common()[:-n-1:-1]#Boy
# f.most_common(25)#Girl
# f.most_common()[:-25-1:-1]#Boy



# stopWords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
# stopWords +=['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']
# stopWords +=['document','cdata','author','lang','en']
# stopWords= [ps.stem(w) for w in stopWords]

import io
# with io.open("GirlAll.txt", 'w', encoding='utf8') as fout:
	# for w in str_listF:
		# if w not in stopWords  and len(w) in range(4,10):
			# fout.write(w+' ')
# with io.open("BoyAll.txt", 'w', encoding='utf8') as fout:
	# for w in str_listM:
		# if w not in stopWords  and len(w) in range(4,10):
			# fout.write(w+' ')

with io.open("HumanTop100Stem.txt", 'w', encoding='utf8') as fout:
	for (w,fr) in om.most_common(100):
		fout.write(w+' ')
with io.open("BotTop100Stem.txt", 'w', encoding='utf8') as fout:
	for (w,fr) in om.most_common()[:-100-1:-1]:
		fout.write(w+' ')


f=Counter(str_listF)
m=Counter(str_listM)
#Varianta 2: luam care au aparut de cel putin 200 ori, dar nu mai mult de 1000 (ca dupaia sunt stopwords)
filterF = {k:v for (k,v) in dict(f).items() if v>200 and v<1000}#nici prea populare (stopwords)
filterM = {k:v for (k,v) in dict(m).items() if v>200 and v<1000}#nici prea nefolosite 
#si facand diferenta: obtinem fotbal,beer,car,game,hit,huge la baieti si "wish, summer, girl" la fete :
#!!!! set(filterF).difference(set(filterM)) !interesant

# for words in unique_words : 
	# if(str_list.count(words)>100):
		# print(words , '-', str_list.count(words)) 
		

#https://stackoverflow.com/questions/23862406/filter-items-in-a-python-dictionary-where-keys-contain-a-specific-string
#https://docs.python.org/2/library/collections.html
#https://stackoverflow.com/questions/5493073/python-read-huge-file-line-by-line-with-utf-8-encoding
#https://www.geeksforgeeks.org/python-string-split/
#https://pair-code.github.io/facets/

#https://gist.github.com/sebleier/554280
#https://pythonspot.com/nltk-stop-words/
#https://stackoverflow.com/questions/2152898/filtering-a-list-of-strings-based-on-contents
#https://stackoverflow.com/questions/20510768/count-frequency-of-words-in-a-list-and-sort-by-frequency
