class NuSVClassifier(object):
    def __init__(self, language, test_path):
        self.language = language
        self.test_path = test_path
        self.train_path = './data/raw/' + language + '/'
        self.kernel_path = './data/processed' + language + '/'

        self.create_kernel()

    def create_kernel(self):
        pass

    def fit(self):
        pass

    def predict(self):
        return [Prediction('b2d5748083d6fdffec6c2d68d4d4442d', self.language, 0),
                Prediction('2bed15d46872169dc7deaf8d2b43a56', self.language, 0),
                Prediction('8234ac5cca1aed3f9029277b2cb851b', self.language, 2),
                Prediction('5ccd228e21485568016b4ee82deb0d28', self.language, 2),
                Prediction('60d068f9cafb656431e62a6542de2dc0', self.language, 1),
                Prediction('c6e5e9c92fb338dc0e029d9ea22a4358', self.language, 1)]


class Prediction(object):
    def __init__(self, author_id, language, value):
        self.id = author_id
        self.lang = language
        self.__set_type_gender(value)

    def __set_type_gender(self, value):
        if value == 0:
            self.type = 'bot'
            self.gender = 'bot'
        elif value == 1:
            self.type = 'human'
            self.gender = 'male'
        elif value == 2:
            self.type = 'human'
            self.gender = 'female'
