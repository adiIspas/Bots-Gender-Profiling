import sys

import model
import rw_operations

language = sys.argv[1]
test_path = sys.argv[2]

print('Run with params\n language:', language, '\n', 'test_path:', test_path)

classifier = model.NuSVClassifier(language, test_path, True)
classifier.fit()

predictions = classifier.predict()
rw_operations.save_predictions(predictions, language)
