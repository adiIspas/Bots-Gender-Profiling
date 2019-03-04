import numpy as np
import matplotlib.pyplot as plt

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.preprocessing import normalize
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

models = [('LR', LogisticRegression(solver='lbfgs')),
          ('LDA', LinearDiscriminantAnalysis()),
          ('Knn3', KNeighborsClassifier(3)),
          ('Knn5', KNeighborsClassifier(5)),
          ('LSVM', SVC(kernel="linear")),
          ('RBF SVM', SVC(gamma=1.6, C=3.5, tol=0.1)),
          ('DT', DecisionTreeClassifier(max_depth=5)),
          ('RF', RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)),
          ('NN', MLPClassifier(alpha=1)),
          ('AB', AdaBoostClassifier()),
          ('NB', GaussianNB()),
          ('QDA', QuadraticDiscriminantAnalysis())]

csv_file = open("../../data/processed/en/en_data.csv")
features_name = csv_file.readline().split(',')
features_name.pop(-1)
data = np.loadtxt(csv_file, delimiter=",")

# features_indexes = [2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # specified feature
# X = data[:, features_indexes]  # specified feature
X = data[:, :-1]

y = data[:, -1]
y = np.transpose([round(x / 2.0 + 0.1) for x in y])

# We can try with normalize data
X = normalize(X)

results = []
names = []
mods = []
for name, model in models:
    k_fold = model_selection.StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
    cv_results = model_selection.cross_val_score(model, X, y, cv=k_fold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

best_index = np.array([x.mean() for x in results]).argsort()[::-1][:10]
results = np.array(results)[best_index]
names = np.array(names)[best_index]

fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results.tolist())
ax.set_xticklabels(names)
plt.show()
