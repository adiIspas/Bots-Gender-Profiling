import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import ExtraTreesClassifier


def feature_importance(print_plot=True):
    csv_file = open("../../data/processed/en/en_data.csv")
    features_name = csv_file.readline().split(',')
    features_name.pop(-1)

    data = np.loadtxt(csv_file, delimiter=",")

    x = data[:, :-1]
    y = data[:, -1]
    y = np.transpose([round(x / 2.0 + 0.1) for x in y])

    # Build a forest and compute the feature importance
    forest = ExtraTreesClassifier(n_estimators=250, random_state=0)
    forest.fit(x, y)

    importance = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
    indices = np.argsort(importance)[::-1]

    if print_plot is True:
        # Print the feature ranking
        print("Feature ranking:")
        for csv_file in range(x.shape[1]):
            print("%d. feature %s (%f)" % (csv_file + 1, features_name[indices[csv_file]], importance[indices[csv_file]]))

        # Plot the feature importance of the forest
        plt.figure()
        plt.title("Feature importance")
        plt.bar(range(x.shape[1]), importance[indices], color="r", yerr=std[indices], align="center")
        plt.xticks(range(x.shape[1]), indices)
        plt.xlim([-1, x.shape[1]])
        plt.show()

    return indices


feature_importance()
