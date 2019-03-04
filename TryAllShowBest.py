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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

models = []
models.append(('LR', LogisticRegression(solver='lbfgs')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='scale')))

models.append(('Knn2', KNeighborsClassifier(4)))
models.append(('LSVM', SVC(gamma='scale', kernel="linear", C=0.025)))
models.append(('RBF SVM', SVC(gamma=1.6, C=3.5, tol=0.1)))
models.append(('Gaussian Process', GaussianProcessClassifier(1.0 * RBF(1.0))))
models.append(('DT', DecisionTreeClassifier(max_depth=5)))
models.append(('RF', RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)))
models.append(('NN', MLPClassifier(alpha=1)))
models.append(('AB', AdaBoostClassifier()))
models.append(('NB', GaussianNB()))
models.append(('QDA', QuadraticDiscriminantAnalysis()))

# f = open("x_features.txt")
# Features=f.readline().split(',')
# data = np.loadtxt(f,delimiter=",")
# Y=data[:,0]
# X=data[:,1:]
# Features.pop(0)#Primu e clasa

f = open("./data/processed/en/en_data.csv")
Features = f.readline().split(',')
data = np.loadtxt(f, delimiter=",")
Features.pop(-1)  # ultimu e clasa
Y = data[:, -1]
X = data[:, :-1]
Y = np.transpose([round(x / 2.0 + 0.1) for x in Y])
# Y = [round(x / 2.0 + 0.1) for x in Y]

results = []
names = []
scoring = 'accuracy'
for name, model in models:
    kfold = model_selection.StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

# clf = SVC(gamma=1.6, C=3.5, tol=0.1)
# results = []
# for i in range(0, 100):
#     X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
#
#     clf.fit(X_train, y_train)
#     results.append(clf.score(X_test, y_test))
#
# results = sorted(results)
# plt.plot(results)
# plt.title('Accuracy evolution')
# plt.show()
# print('Min accuracy', min(results))
# print('Mean accuracy after', len(results), 'iterations is ', np.mean(results))
# print('Max accuracy', max(results))

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

reduced_data = PCA(n_components=2).fit_transform(X)
kmeans = KMeans(init='k-means++', n_clusters=2, n_init=10)
kmeans.fit(reduced_data)
cmap_bold = ListedColormap(['#FF0000', '#00FF00'])
# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=7)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)
plt.title('K-means')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
