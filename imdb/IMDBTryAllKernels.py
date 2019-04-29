from collections import Counter
import numpy as np


def KernelFrom2ListsK3RN3L(A, B):
    ret = 0
    if (len(A) < len(B)):
        for pair in A.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += a / b
            else:
                ret += b / a
    else:
        for pair in B.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += a / b
            else:
                ret += b / a
    return ret


def KernelFrom2ListsK3RN3LSqared(A, B):
    ret = 0
    if (len(A) < len(B)):
        for pair in A.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += pow(a / b, 2)
            else:
                ret += pow(b / a, 2)
    else:
        for pair in B.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += pow(a / b, 2)
            else:
                ret += pow(b / a, 2)
    return ret


def KernelFrom2ListsK3RN3LSQRT(A, B):
    ret = 0
    if (len(A) < len(B)):
        for pair in A.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += pow(a / b, 0.5)
            else:
                ret += pow(b / a, 0.5)
    else:
        for pair in B.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += pow(a / b, 0.5)
            else:
                ret += pow(b / a, 0.5)
    return ret


def KernelFrom2ListsIntersect(A, B):
    ret = 0
    if (len(A) < len(B)):
        for pair in A.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += a
            else:
                ret += b
        # ret+=min(A[pair],B[pair])
    else:
        for pair in B.keys():
            a = A[pair]
            b = B[pair]
            if (a < b):
                ret += a
            else:
                ret += b
    return ret


def KernelFrom2ListsSpectrum(A, B):
    ret = 0
    if (len(A) < len(B)):
        for pair in A.keys():
            ret += (1 + A[pair]) * (1 + B[pair])
    else:
        for pair in B.keys():
            ret += (1 + A[pair]) * (1 + B[pair])
    return ret


def KernelFrom2ListsPresence(A, B):
    ret = 0
    if (len(A) < len(B)):
        for pair in A.keys():
            if (B[pair] != 0):
                ret += 1
    else:
        for pair in B.keys():
            if (A[pair] != 0):
                ret += 1
    return ret


def File2Pgrams(file, pgram=2):
    # print(file)
    # oneLongTweet = open(file,encoding='utf8').read()
    oneLongTweet = open(file, encoding='ISO-8859-1').read()
    oneLongTweet = oneLongTweet.lower()
    oneLongTweet = ' '.join(oneLongTweet.split())
    return Counter([oneLongTweet[i:i + pgram] for i in range(0, len(oneLongTweet) - pgram + 1)])


from sklearn.svm import NuSVC
from math import sqrt
import os
import time

DIR = "20"

fout = open("Procent = " + DIR + " - " + str(time.time()), 'w')
FilesTrain = [DIR + '/train/' + file for file in os.listdir(DIR + '/train')]
FilesTest = [DIR + '/test/' + file for file in os.listdir(DIR + '/test')]

N_Train = len(FilesTrain)
N_Test = len(FilesTest)
N = N_Train + N_Test

Kernel = np.empty([N, N], dtype=float)
Cache = np.empty([N, ], dtype=object)
Y = np.empty([N, ], dtype=int)

for pgram in range(3, 13):  # 2
    print('Current p_gram:', pgram)

    for normalizare in [False, True]:
        if pgram == 3 and normalizare is False:
            continue

        print('Normalize:', normalizare)

        i = 0
        for file in FilesTrain + FilesTest:

            if int(file[-5]) > 5:
                Y[i] = 1
            else:
                Y[i] = 0

            Cache[i] = File2Pgrams(file, pgram)
            if normalizare:
                norma = 1 + sum(Cache[i].values())
                for pair in Cache[i].keys():
                    Cache[i][pair] /= norma
            i = i + 1

        for kernelFunc in [KernelFrom2ListsK3RN3L, KernelFrom2ListsK3RN3LSQRT, KernelFrom2ListsK3RN3LSqared,
                           KernelFrom2ListsIntersect, KernelFrom2ListsSpectrum, KernelFrom2ListsPresence]:  # 3

            # continue execution after a break
            if pgram == 3 and normalizare is True and kernelFunc.__name__ in ['KernelFrom2ListsK3RN3L', 'KernelFrom2ListsK3RN3LSQRT', 'KernelFrom2ListsK3RN3LSqared', 'KernelFrom2ListsIntersect']:
                continue

            print('Kernel function:', kernelFunc.__name__)
            for i in range(N):
                for j in range(i, N):
                    Kernel[i][j] = kernelFunc(Cache[i], Cache[j])
                    Kernel[j][i] = Kernel[i][j]
            # normalizare
            for i in range(N):
                for j in range(N):
                    if (i != j):
                        Kernel[i][j] /= sqrt(Kernel[i][i] * Kernel[j][j] + 1)
            for i in range(N):
                Kernel[i][i] = 1

            AccMax = 0
            for nu in [0.4, 0.25, 0.1, 0.07]:  # 4
                clf = NuSVC(nu, kernel='precomputed', )  # ,#verbose =True,      shrinking=False,
                clf.fit(Kernel[0:N_Train, 0:N_Train], Y[0:N_Train])
                # AccTrain=(clf.predict(Kernel[0:N_Train,0:N_Train])==Y[0:N_Train]).mean()
                AccTest = (clf.predict(Kernel[N_Train:, 0:N_Train]) == Y[N_Train:]).mean()
                AccMax = max(AccMax, AccTest)
            # print('nu= ',nu,' acc pe train: ' ,AccTrain,' Acc pe test: ',AccTest)
            print(pgram, normalizare, kernelFunc.__name__, AccMax)
            print(pgram, normalizare, kernelFunc.__name__, AccMax, file=fout, flush=True)
