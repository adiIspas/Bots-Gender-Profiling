import os
import xml.etree.ElementTree as ET


def save_predictions(predictions, language):
    if not os.path.exists(language):
        os.makedirs(language)

    for prediction in predictions:
        data = ET.Element('author')
        data.set('id', prediction.id)
        data.set('lang', prediction.lang)
        data.set('type', prediction.type)
        data.set('gender', prediction.gender)

        author_file = open(language + '/' + prediction.id + '.xml', 'wb')
        author_file.write(ET.tostring(data))
