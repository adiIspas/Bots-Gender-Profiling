import shutil

dataset_path = './data/raw/en/'
path_train = './data/raw/en/truth-train.txt'
path_test = './data/raw/en/truth-dev.txt'
test_path = './test/'
train_path = './train/'

with open(path_train, 'r') as train_file:
    files = train_file.readlines()

    for file in files:
        filename = file.split(':::')[0] + '.xml'
        shutil.copy(dataset_path + filename, train_path + filename)

with open(path_test, 'r') as test_file:
    files = test_file.readlines()

    for file in files:
        filename = file.split(':::')[0] + '.xml'
        shutil.copy(dataset_path + filename, test_path + filename)
