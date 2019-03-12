import re

import emoji
import pyphen
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


class Features(object):

    def __init__(self, language):
        self.language = language
        self.languages_name_dict = {'en': 'english', 'es': 'spanish'}
        self.languages_iso_dict = {'en': 'en_UK', 'es': 'es_ES'}

        self.stop_words = stopwords.words(self.languages_name_dict.get(self.language))
        self.syllables_dic = pyphen.Pyphen(lang=self.languages_iso_dict.get(self.language))
        self.stemmer = SnowballStemmer(self.languages_name_dict.get(language))

        self.en_bot_popular_words = ['http', 'co', 't', 'job', 'develop', 'engin', 'softwar', 'manag', 'hire', 'senior',
                                     'locat', 'descript', 'career', 'system', 'tech', 'techjob', 'itjob', 'analyst',
                                     'technolog', 'ly', 'servic', 'project', 'applic', 'busi', 'compani', 'and',
                                     'posit', 'data', 'java', 'experi', 'design', 'lead', 'medic', 'solut', 'respons',
                                     'full', 'net', 'sr', 'histori', 'technic', 'support', 'provid', 'bit', 'learn',
                                     'network', 'tip', 'team', 'id', 'picard', 'comput', 'read', 'is', 'consult',
                                     'health', 'client', 'seek', 'check', 'product', 'requir', '0', 'test', 'secur',
                                     'introduct', 'scrum', 'date', 'us', 'web', 'architect', 'inform', 'inc', 'com',
                                     'detail', 'type', '18', 'python', 'custom', 'market', 'opportun', 'sql', 'site',
                                     'gt', 'contract', 'program', 'california', 'oper', 'master', 'specialist', '2018',
                                     'unit', 'titl', 'avail', 'administr', 'shoe', 'autom', 'level', 'will', 'nurs',
                                     'state', 'enterpris', 'ca']

        self.en_human_popular_words = ['rt', 'i', 'the', 'to', 'thi', 'my', 'on', 'so', 'that', 'thank', 'just', 'me',
                                       'in', 'a', 'you', 'have', 'but', 'be', 'like', 'wa', 'from', 'for', 'at', 'all',
                                       'get', 'day', 'up', 's', 'go', 'i\'m', 'not ', 'can', 'they', 'today', 'love',
                                       'good', 'here', 'how', 'what', 'he', 'back', 'hi', 'been', 'now', 'it\'',
                                       'there', 'think', ' if ', 'when', 'fuck', 'had', 'last', 'her', 'm', 'would',
                                       'some', 'night', 'see', 'year', 'say', 'come', 'too', 'know', 'realli',
                                       'tonight',
                                       'still', 'vote', 'video', 'did', 'she', 'much', 'hope', 'happi', 'watch', 'do',
                                       'right', 'off', 'well', 'one', 'out', 'them', 'even', 'win', 'morn', 'ye',
                                       'mailonlin', 'also', 'next', 'x', 'take', 'i\'v', 'no', 'week', 'peopl', 'feel',
                                       'should', 'could', 'sure', 'actual', 'done']

        self.en_male_popular_words = ['the', 't', 'http', 'co', 'to', 'a', 'rt', 'of', 'and', 'in', 'i', 'is', 'for',
                                      'you', 'it', 'on', 'thi', 'that', 'be', 'my', 'with', 'at', 'have', 'are', 'but',
                                      'not', 'wa', 's', 'we', 'from', 'just', 'so', 'get', 'as', 'all', 'what', 'your',
                                      'me', 'if', 'out', 'like', 'do', 'about', 'up', 'they', 'one', 'will', 'by',
                                      'can', 'he', 'an', 'new', 'go', 'time', 'no', 'ha', 'it\'', 'thank', 'now', 'day',
                                      'good', 'how', 'amp', 'when', 'hi', 'look', 'year', 'more', 'who', ' or ', 'our',
                                      'see', 'there', 'think', 'great', 'make', 'love', 'peopl', 'i\'m', 'know', 'work',
                                      'say', 'today', 'need', 'some', 'would', 'been', 'back', 'don\'t', 'come', '2',
                                      'want', 'here', 'take', 'their', '1', 'thing', 'them', 'trump', 'well']

        self.en_female_popular_words = ['t', 'http', 'co', 'the', 'rt', 'to', 'a', 'and', 'i', 'of', 'in', 'you', 'for',
                                        'is', 'on', 'it', 'thi', 'my', 'that', 'with', 'be', 'your', 'at', 'have',
                                        'are', 'so', 's', 'me', 'we', 'just', 'amp', 'can', 'all', 'from', 'not', 'wa',
                                        'but', 'thank', 'about', 'get', 'like', 'what', 'our', 'do', 'as', 'love', 'if',
                                        'by', 'day', 'how', 'out', 'up', 'one', 'an', 'will', 'time', 'when', 'go',
                                        'peopl', 'who', 'they', 'hi', 'ha', 'new', 'no', 'more', 'year', 'now', 'today',
                                        'work', 'i\'m', 'make', 'it\'', 'look', 'he', 'know', 'see', 'here', 'there',
                                        'good', 'say', 'video', 'her', 'back', 'or', 'think', 'need', 'their', 'been',
                                        'great', 'want', 'use', 'pleas', 'us', 'right', 'would', 'some', 'she', 'm',
                                        'them']

        self.en_bot_human_popular_words = ['http', 'co', 't', 'job', 'develop', 'engin', 'softwar', 'manag', 'hire',
                                           'and', 'senior', 'locat', 'descript', 'career', 'system', 'is', 'tech', 'of',
                                           'techjob', 'technolog', 'itjob', 'analyst', 'servic', 'ly', 'project',
                                           'busi', 'applic', 'compani', 'posit', 'data', 'experi', 'java', 'design',
                                           'lead', 'medic', 'solut', 'respons', 'full', 'support', 'histori', 'net',
                                           'sr', 'provid', 'technic', 'bit', 'learn', 'team', 'network', 'tip', 'read',
                                           'us', 'id', 'check', 'comput', 'health', 'picard', 'consult', 'product',
                                           'client', 'seek', '0', 'requir', 'will', 'test', 'secur', 'date',
                                           'introduct', 'scrum', 'with', 'web', 'architect', 'inform', 'inc', 'market',
                                           'detail', '18', 'com', 'type', 'custom', 'gt', 'opportun', 'python', 'site',
                                           'sql', 'contract', '2018', '1', 'program', 'work', 'our', 'california',
                                           'oper', 'master', 'unit', 'specialist', 'avail', 'titl', 'administr',
                                           'state', 'it']

        self.en_human_bot_popular_words = ['rt', 'i', 'thi', 'my', 'to', 'on', 'the', 'so', 'thank', 'that', 'just',
                                           'me', 'but', 'like', 'have', 'from', 'wa', 'be', 'all', 'day', 'i\'m', 'up',
                                           'go', 'get', 'at', 'today', 'here', 's', 'can', 'good', 'love', 'they',
                                           'not', 'back', 'how', 'been', 'he', 'fuck', 'you', 'in', 'hi', 'now', 'it\'',
                                           'think', 'm', 'what', 'there', 'had', 'night', 'last', 'her', 'would',
                                           'some', 'when', 'tonight', 'see', 'say', 'vote', 'too', 'if', 'realli',
                                           'come', 'still', 'year', 'did', 'she', 'hope', 'video', 'much', 'happi',
                                           'know', 'watch', 'morn', 'off', 'mailonlin', 'well', 'even', 'ye', 'right',
                                           'win', 'x', 'also', 'them', 'i\'v', 'next', 'for', 'actual', 'sure', 'feel',
                                           'done', 'amaz', 'week', 'wait', 'could', 'take', 'tomorrow', 'don', 'should',
                                           'show', 'final']

        self.en_male_female_popular_words = ['the', 'a', 'that', 'is', 'it', 'he', 'but', 'game', 'be', 'they', 'not',
                                             'for', 'play', 'it\'', 'good', 'fuck', 'as', 'out', 'man', '_tessathoma',
                                             'or', 'no', 'new', 'if', 'team', 'him', 'vancouv', 'he\'', 'in', 'fan',
                                             'what', 'of', 'gt', 'mate', 'that\'', 'will', 'win', 'wa', 'great',
                                             'don\'t', 'at', 'season', 'fundris', 'well', 'trump', 'get', 'think',
                                             'some', 'look', 'leagu', 'ha', '2', 'got', 'goal', 'point', 'boardoftrad',
                                             'babyboom', 'big', 'one', 'up', 'from', 'see', 'ani', 'go', 'than',
                                             'there', 'stanleycup', 'would', 'nice', 'come', 'also', 'beer', 'now',
                                             'time', 'footbal', '1', 'johnbdeleo', '0', 'cup', 'onli', 'though', 'guy',
                                             'celtic', 'should', 'citi', 'club', 'off', 'score', 'then', 'lad',
                                             'eritrea', 'first', 'sure', 'car', 'paint', 'might', 'two', 'sign',
                                             'again', '3']

        self.en_female_male_popular_words = ['rt', 't', 'http', 'you', 'co', 'to', 'i', 'your', 'amp', 'and', 'video',
                                             'so', 'mailonlin', 'love', 'our', 'can', 'my', 'me', 'thank', 'social',
                                             'her', 'women', 'pleas', 'u', 's', 'she', 'with', 'thejournal_i',
                                             'comment', 'girl', 'youtub', 'peopl', 'how', 'find', 'x', 'via',
                                             'immersivemind', 'day', 'vichislop', 'happi', 'life', 'facebook', 'm',
                                             'app', 'screen', 'mvsgrperli', 'term', 'today', 'dm', 'about',
                                             'girlstream', 'innov', 'xx', 'media', 'oyvj3tkix8', 'grab', 'feel',
                                             'footag', 'account', 'fulli', 'law', 'here', 'credit', 'fcm_onlin',
                                             'eurotoquesirl', 'mariankey', 'homebusi', 'woman', 'busi', 'food',
                                             'we\'ll', 'newsflar', 'market', 'morn', 'vickinotaro', 'school', 'send',
                                             'instagram', 'de', 'networkmarket', 'hootsuit', 'don', 'work', 'shaunamp',
                                             'help', 'twitchshar', 'holiday', 'are', 'beauti', 'snapchat', 'film',
                                             'omg', 'fab', 'mamaofabean', 'men', 'learn', 'join', '2018', 'stori',
                                             'contact']

        self.es_bot_popular_words = ['de', 'http', 't', 'co', 'la', 'en', 'el', 'a', 'y', 'que', 'lo', 'un', 'del',
                                     'rt', 'no', 'por', 'se', 'con', 'para', 'es', 'una', 'su', 'al', '00', 'si', 'má',
                                     'como', 'me', '2', 'unet', 'teampgv', 'tu', 'ha', 'te', 'año', '1', 'o', 'vía',
                                     '4', 'todo', 'le', 'video', 'esta', '10', 'mi', '5', 'empleo', 'ya', 'día', '000',
                                     '3', 'qué', 'pero', 'está', 'españa', 'est', 'the', 'uno', 'cuando', 'sin',
                                     'trabajo', 'cerca', 'madrid', '7', '0', 'sobr', 'solo', 'do', 'nuevo', 'tien',
                                     'busca', 'ser', 'son', 'hoy', '6', '9', '20', '8', 'mujer', '12', '11', 'vida',
                                     'e', 'os', 'estado', 'hay', 'venta', 'follow', 'mejor', 'yo', 'sigu', 'pued',
                                     'persona', 'hombr', 'nueva', 'c', 'contra', 'ant', 'ind', 'hace']

        self.es_human_popular_words = ['de', 'la', 'http', 'rt', 't', 'co', 'que', 'a', 'el', 'y', 'en', 'lo', 'no',
                                       'es', 'un', 'se', 'por', 'con', 'me', 'para', 'del', 'una', 'mi', 'su', 'te',
                                       'al', 'todo', 'si', 'má', 'como', 'le', 'pero', 'ya', 'q', 'tu', 'día', 'yo',
                                       'esta', 'hoy', 'est', 'cuando', 'o', 'año', 'hay', 'qué', 'ser', 'está', 'tien',
                                       'mejor', 'son', 'porqu', 'eso', 'sin', 'vida', 'gracia', 'esto', 'muy', 'ni',
                                       'ha', 'hace', 'así', 'ahora', 'va', 'solo', 'bien', 'siempr', 'nada', 'ver',
                                       'persona', 'fue', '1', 'pued', 'the', 'quiero', '3', 'mucho', 'uno', 'toda',
                                       'sobr', '2', 'cosa', 'estoy', 'gent', 'd', 'nunca', 'bueno', 'hasta', 'tan',
                                       'hacer', 'tengo', 'vez', 'desd', 'esa', 'dio', 'e', 'do', 'algo', 'nuevo', 'ma',
                                       'quien']

        self.es_male_popular_words = ['de', 'la', 'http', 't', 'co', 'rt', 'que', 'el', 'en', 'a', 'y', 'lo', 'no',
                                      'es', 'un', 'se', 'por', 'con', 'del', 'para', 'una', 'me', 'su', 'al', 'todo',
                                      'má', 'si', 'como', 'le', 'te', 'pero', 'mi', 'est', 'hoy', 'ya', 'esta', 'año',
                                      'o', 'día', 'hay', 'tu', 'qué', 'cuando', 'está', 'ser', 'yo', 'tien', 'q', 'ha',
                                      'son', 'mejor', 'sin', 'gracia', 'eso', 'esto', 'muy', 'hace', 'ni', 'va',
                                      'ahora', 'porqu', '1', 'sobr', 'solo', 'fue', 'the', 'pued', 'así', '2', 'uno',
                                      'bien', '3', 'ver', 'desd', 'vida', 'nada', 'e', 'vía', 'siempr', 'toda', 'mucho',
                                      'contra', 'bueno', 'gobierno', 'hasta', 'paí', 'persona', 'do', 'nuevo',
                                      'partido', 'vez', 'gent', 'ant', 'ma', 'otro', 'venezuela', 'nuestro', 'esa',
                                      'hacer', 'entr']

        self.es_female_popular_words = ['de', 'la', 'rt', 'que', 'http', 't', 'co', 'a', 'y', 'no', 'el', 'en', 'lo',
                                        'me', 'es', 'un', 'se', 'por', 'con', 'para', 'mi', 'una', 'te', 'del', 'si',
                                        'todo', 'su', 'como', 'q', 'al', 'má', 'le', 'pero', 'yo', 'tu', 'ya', 'día',
                                        'cuando', 'esta', 'o', 'hoy', 'est', 'hay', 'qué', 'ser', 'vida', 'año',
                                        'porqu', 'está', 'mejor', 'son', 'tien', 'eso', 'sin', 'así', 'quiero', 'esto',
                                        'estoy', 'muy', 'ni', 'persona', 'gracia', 'siempr', 'hace', 'tengo', 'ahora',
                                        'bien', 'nada', 'dio', 'va', 'solo', 'cosa', 'nunca', 'ver', 'mucho', 'toda',
                                        'd', 'tan', 'ha', 'gent', 'amor', 'hacer', 'soy', '3', 'pued', 'voy', 'fue',
                                        'uno', 'esa', 'the', 'bueno', 'feliz', 'algo', 'hasta', '1', 'vez', 'alguien',
                                        'mañana', 'quien', '2']

        self.es_bot_human_popular_words = ['co', 't', 'http', 'de', 'en', 'el', 'la', '00', 'del', 'unet', 'teampgv',
                                           '2', 'un', 'empleo', 'video', '4', 'vía', '000', '10', 'ha', 'españa',
                                           'cerca', '1', '5', 'su', 'busca', 'madrid', 'venta', '0', '7', 'ind',
                                           'trabajo', 'os', '12', '9', 'km', '11', 'tráfico', 'registrado', 'ar',
                                           'desaparec', 'ad', 'ft', '8', 'aparecido', 'mn', 'tráficogt', 'trafficbotgt',
                                           'dime_chiko', 'eb', 'sismo', 'cp', 'rc', '20', 'salvaj', 'ccdbot', 'am',
                                           'tt', 'ajnew', 'amp', 'observador', 'oferta', 'rm', 'ipautaorg', 'seguidor',
                                           'follow', 'hr', 'report', 'vinilo', 'empleoticjob', '6', 'atraco', 'sigu',
                                           'difund', 'android', 'guatemala', 'empleot', 'inc', 'piso', 'tra', 'oacuten',
                                           'condici', 'max', '01', 'marianorajoy', 'epicentro', 'san', '3', '15', 'min',
                                           '14', 'tard', 'iphon', 'al', '30', 'hacerfoto', 'estado', '40', 'hombr',
                                           'worldwid']

        self.es_human_bot_popular_words = ['rt', 'que', 'no', 'me', 'y', 'es', 'mi', 'q', 'todo', 'lo', 'te', 'pero',
                                           'le', 'yo', 'hoy', 'ya', 'eso', 'con', 'hay', 'cuando', 'se', 'esto', 'est',
                                           'porqu', 'a', 'día', 'va', 'quiero', 'ser', 'muy', 'estoy', 'mejor', 'ni',
                                           'ahora', 'gracia', 'esa', 'siempr', 'gent', 'así', 'tengo', 'bien', 'nada',
                                           'esta', 'por', 'tien', 'feliz', 'son', 'hace', 'dio', 'voy', 'x', 'nunca',
                                           'algo', 'cosa', 'mucho', 'ver', 'tan', 'bueno', 'toda', 'buena', 'si', 'qué',
                                           'vida', 'ese', 'mañana', 'soy', 'd', 'vamo', 'como', 'hacer', 'creo', 'paí',
                                           'jajaja', 'quien', 'sea', 'estar', 'ir', 'fue', 'tanto', 'jajajaja', 'está',
                                           'buen', 'puedo', 'amo', 'vez', 'nadi', 'mucha', 'tener', 'igual', 'nuestro',
                                           'he', 'ahí', 'gusta', 'momento', 'mismo', 'vo', 'estamo', 'pasa',
                                           'venezuela', 'para']

        self.es_male_female_popular_words = ['de', 'el', 'en', 'la', 'http', 'co', 't', 'del', 'al', 'su', 'by',
                                             'ministerio_t', 'vía', 'via', 'gobierno', 'partido', 'ha',
                                             'marisabelmejia', 'españa', 'contra', 'con', 'madrid', 'equipo',
                                             'venezuela', 'se', 'call', 'carrera', 'sobr', 'jugador', 'desd', 'c0nvey',
                                             'rmbaloncesto', 'dolartoday', 'mundial', 'epigmenioibarra', 'gran',
                                             'check', 'president', 'un', 'automat', 'entr', 'e', 'año', 'unfollow',
                                             'albmaldonadook', 'ganarlegan', 'rmtv', 'sur', 'leofabi36', 'millon',
                                             'prensa', 'paí', 'política', '000', 'universitario', 'ijfe0h93sc', 'psoe',
                                             'follow', 'rueda', 'h', 'person', '6', '2', 'hipismo', 'fútbol', 'han',
                                             'pp', 'barrio', 'copa', 'river', '1', 'nueva', 'militar', 'nort', 'festiv',
                                             'maduro', 'gol', 'final', 'jfbejarano', 'sí', 'est', 'tkpvjdkwpu',
                                             'independient', 'jugar', 'legan', 'labuenavidalib', 'público', 'tv',
                                             'transito', 'temporada', 'lunadavid', 's', 'lima', 'ministro', '4',
                                             'domingo', 'vs', 'nacion', 'pcelegan', 'one']

        self.es_female_male_popular_words = ['me', 'no', 'que', 'mi', 'te', 'q', 'yo', 'tu', 'si', 'y', 'rt', 'cuando',
                                             'es', 'estoy', 'día', 'vida', 'tengo', 'todo', 'ya', 'quiero', 'dio', 'a',
                                             'porqu', 'voy', 'pero', 'amor', 'soy', 'persona', 'nunca', 'feliz', 'lo',
                                             'cosa', 'como', 'así', 'siempr', 'alguien', 'tan', 'jnunezlazcano',
                                             'radiozeta_cl', 'd', 'i', 'jajaja', 'amiga', 'puedo', 'jaja', 'mejor',
                                             'pisci', 'you', 'amo', 'algo', 'le', 'nada', 'ir', 'hacer', 'leyvscorazon',
                                             'tú', 'ser', 'laurabarrera99', 'girlzandi', 'una', 'esta', 'esa',
                                             'instalik', 'gent', 'bien', 'mucho', 'eso', 'estar', 'lt', 'dormir',
                                             'vece', 'sé', 'o', 'jajajaja', 'guatonfantasma', 'corazón', 'igualeschil',
                                             'lindo', 'toda', 'instachil', 'sabe', 'mañana', 'necesito', 'gana', 'ella',
                                             'ay', 'amigo', 'nadi', 'casa', 'mamá', 'team_yoz', 'quier', 'servitributo',
                                             'mal', 'libro', 'laleydelcorazon', 'ti', 'lucianoda', 'da', 'gusta']

        self.en_free_words = ['free', 'givaway', 'gift', 'follow', 'win', 'change', 'winner', 'subscribe', 'comment',
                              'retweet', 'competition']

        self.es_free_words = ['gratis', 'givaway', 'regalo', 'seguir', 'ganar', 'cambiar', 'ganador', 'suscribirse',
                              'comentar', 'retweet', 'competición']

        self.en_political_words = ['politics', 'donald', 'Vladimir', 'trump', 'putin', 'obama', 'Us', 'USA', 'Russia',
                                   'Clinton', 'Hillary', 'politicians', 'Catalonia', 'President', 'American', 'ISIS',
                                   'office', 'legislation', 'Testify', 'Oath', 'scandal', 'CIA', 'CNN', 'FOX', 'video',
                                   'Ceremony', 'Congress', 'budget', 'Administration', 'democrats', 'vote', 'rights']

        self.es_political_words = ['Política', 'Donald', 'Vladimir', 'Trump', 'Putin', 'Obama', 'Europa', 'Clinton',
                                   'Hillary', 'políticos', 'Cataluña', 'Presidente', 'América', 'ISIS', 'oficina',
                                   'legislación', 'Testificar', 'Juramento', 'escándalo', 'CIA', 'CNN', 'FOX', 'video',
                                   'Ceremonia', 'Congreso', 'Presupuesto', 'Administración', 'Demócratas', 'Voto',
                                   'Derechos']

    def extract(self, tweets):
        number_of_words = 0
        number_of_characters = 0
        average_word_len = 0
        number_of_stop_words = 0
        number_of_tags = 0
        number_of_hash_tags = 0
        number_of_syllables = 0
        number_of_secure_links = 0
        number_of_unsecured_links = 0
        number_of_digits = 0
        number_of_percent = 0
        number_of_exclamation_marks = 0
        number_of_question_marks = 0
        number_of_commas = 0
        number_of_points = 0
        number_of_emoji = 0
        number_of_tildes = 0
        number_of_dollars = 0
        number_of_circumflex_accents = 0
        number_of_ampersands = 0
        number_of_stars = 0
        number_of_parenthesis = 0
        number_of_minuses = 0
        number_of_underscores = 0
        number_of_equals = 0
        number_of_pluses = 0
        number_of_brackets = 0
        number_of_curly_brackets = 0
        number_of_vertical_bars = 0
        number_of_semicolons = 0
        number_of_colons = 0
        number_of_apostrophes = 0
        number_of_grave_accents = 0
        number_of_quotation_marks = 0
        number_of_slashes = 0
        number_of_less_grater_than_signs = 0
        number_of_words_in_bot_popular_words = 0
        number_of_words_in_human_popular_words = 0
        number_of_words_in_male_popular_words = 0
        number_of_words_in_female_popular_words = 0
        number_of_words_in_bot_human_popular_words = 0
        number_of_words_in_human_bot_popular_words = 0
        number_of_words_in_male_female_popular_words = 0
        number_of_words_in_female_male_popular_words = 0
        number_of_lines = 0
        number_of_money = 0
        number_of_words_start_with_capital_letter = 0
        number_of_free_words = 0
        number_of_political_words = 0

        different_words = set()
        total_tweets = len(tweets)
        longest_repeated_str = self.longest_repeated_substring(' '.join(tweets))

        for tweet in tweets:
            number_of_words += self.number_of_words_per_tweet(tweet)
            number_of_characters += self.number_of_characters_per_tweet(tweet)
            average_word_len += self.average_word_len_per_tweet(tweet)
            number_of_stop_words += self.number_of_stop_words_per_tweet(tweet)
            number_of_tags += self.number_of_tags_per_tweet(tweet)
            number_of_hash_tags += self.number_of_hash_tags_per_tweet(tweet)
            number_of_syllables += self.number_of_syllables_per_tweet(tweet)
            number_of_digits += self.number_of_digits_per_tweet(tweet)
            number_of_secure_links += self.number_of_secure_links_per_tweet(tweet)
            number_of_unsecured_links += self.number_of_unsecured_links_per_tweet(tweet)
            number_of_percent += self.number_of_percent_per_tweet(tweet)
            number_of_exclamation_marks += self.number_of_exclamation_marks_per_tweet(tweet)
            number_of_question_marks += self.number_of_question_marks_per_tweet(tweet)
            number_of_commas += self.number_of_commas_per_tweet(tweet)
            number_of_points += self.number_of_points_per_tweet(tweet)
            number_of_emoji += self.number_of_emoji_per_tweet(tweet)
            number_of_tildes += self.number_of_tilde_per_tweet(tweet)
            number_of_dollars += self.number_of_dollars_per_tweet(tweet)
            number_of_circumflex_accents += self.number_of_circumflex_accents_per_tweet(tweet)
            number_of_ampersands += self.number_of_ampersands_per_tweet(tweet)
            number_of_stars += self.number_of_stars_per_tweet(tweet)
            number_of_parenthesis += self.number_of_parenthesis_per_tweet(tweet)
            number_of_minuses += self.number_of_minuses_per_tweet(tweet)
            number_of_underscores += self.number_of_underscores_per_tweet(tweet)
            number_of_equals += self.number_of_equals_per_tweet(tweet)
            number_of_pluses += self.number_of_pluses_per_tweet(tweet)
            number_of_brackets += self.number_of_brackets_per_tweet(tweet)
            number_of_curly_brackets += self.number_of_curly_brackets_per_tweet(tweet)
            number_of_vertical_bars += self.number_of_vertical_bars_per_tweet(tweet)
            number_of_semicolons += self.number_of_semicolons_per_tweet(tweet)
            number_of_colons += self.number_of_colons_per_tweet(tweet)
            number_of_apostrophes += self.number_of_apostrophes_per_tweet(tweet)
            number_of_grave_accents += self.number_of_grave_accents_per_tweet(tweet)
            number_of_quotation_marks += self.number_of_quotation_marks_per_tweet(tweet)
            number_of_slashes += self.number_of_slashes_per_tweet(tweet)
            number_of_less_grater_than_signs += self.number_of_less_grater_than_signs_per_tweet(tweet)
            number_of_words_in_bot_popular_words += self.number_of_words_in_bot_popular_words_per_tweet(tweet)
            number_of_words_in_human_popular_words += self.number_of_words_in_human_popular_words_per_tweet(tweet)
            number_of_words_in_male_popular_words += self.number_of_words_in_male_popular_words_per_tweet(tweet)
            number_of_words_in_female_popular_words += self.number_of_words_in_female_popular_words_per_tweet(tweet)
            number_of_words_in_bot_human_popular_words += self.number_of_words_in_bot_human_popular_words_per_tweet(
                tweet)
            number_of_words_in_human_bot_popular_words += self.number_of_words_in_human_bot_popular_words_per_tweet(
                tweet)
            number_of_words_in_male_female_popular_words += self.number_of_words_in_male_female_popular_words_per_tweet(
                tweet)
            number_of_words_in_female_male_popular_words += self.number_of_words_in_female_male_popular_words_per_tweet(
                tweet)
            different_words = self.different_words_per_tweet(different_words, tweet)
            number_of_lines += self.number_of_lines_per_tweet(tweet)
            number_of_money += self.number_of_money_per_tweet(tweet)
            number_of_words_start_with_capital_letter += self.number_of_words_start_with_capital_letter_per_tweet(tweet)
            number_of_free_words += self.number_of_free_words_per_tweet(tweet)
            number_of_political_words += self.number_of_political_words_per_tweet(tweet)

        average_number_of_syllables_per_word = number_of_syllables / number_of_words if number_of_words > 0 else 0
        number_of_different_words = len(different_words) / number_of_words if number_of_words > 0 else 0
        number_of_words_per_line = number_of_words / number_of_lines if number_of_lines > 0 else 0
        number_of_words /= total_tweets
        number_of_characters /= total_tweets
        average_word_len /= total_tweets
        number_of_stop_words /= total_tweets
        number_of_tags /= total_tweets
        number_of_hash_tags /= total_tweets
        readability = self.readability_level(number_of_words, average_number_of_syllables_per_word)
        number_of_digits /= total_tweets
        number_of_secure_links /= total_tweets
        number_of_unsecured_links /= total_tweets
        number_of_percent /= total_tweets
        number_of_exclamation_marks /= total_tweets
        number_of_question_marks /= total_tweets
        number_of_commas /= total_tweets
        number_of_points /= total_tweets
        number_of_emoji /= total_tweets
        number_of_tildes /= total_tweets
        number_of_dollars /= total_tweets
        number_of_circumflex_accents /= total_tweets
        number_of_ampersands /= total_tweets
        number_of_stars /= total_tweets
        number_of_parenthesis /= total_tweets
        number_of_minuses /= total_tweets
        number_of_underscores /= total_tweets
        number_of_equals /= total_tweets
        number_of_pluses /= total_tweets
        number_of_brackets /= total_tweets
        number_of_curly_brackets /= total_tweets
        number_of_vertical_bars /= total_tweets
        number_of_semicolons /= total_tweets
        number_of_colons /= total_tweets
        number_of_apostrophes /= total_tweets
        number_of_grave_accents /= total_tweets
        number_of_quotation_marks /= total_tweets
        number_of_slashes /= total_tweets
        number_of_less_grater_than_signs /= total_tweets
        number_of_words_in_bot_popular_words /= total_tweets
        number_of_words_in_human_popular_words /= total_tweets
        number_of_words_in_male_popular_words /= total_tweets
        number_of_words_in_female_popular_words /= total_tweets
        number_of_words_in_bot_human_popular_words /= total_tweets
        number_of_words_in_human_bot_popular_words /= total_tweets
        number_of_words_in_male_female_popular_words /= total_tweets
        number_of_words_in_female_male_popular_words /= total_tweets
        number_of_lines /= total_tweets
        number_of_money /= total_tweets
        number_of_words_start_with_capital_letter /= total_tweets
        number_of_free_words /= total_tweets
        number_of_political_words /= total_tweets
        longest_repeated_str_len = len(longest_repeated_str)
        number_of_longest_repeated_str = ' '.join(tweets).count(longest_repeated_str) / total_tweets
        longest_repeated_str_mix_feature = longest_repeated_str_len * number_of_longest_repeated_str

        return [number_of_words, number_of_characters, average_word_len, number_of_stop_words, number_of_tags,
                number_of_hash_tags, readability, number_of_digits, number_of_secure_links, number_of_unsecured_links,
                number_of_percent, number_of_exclamation_marks, number_of_question_marks, number_of_commas,
                number_of_points, number_of_emoji, number_of_tildes, number_of_dollars, number_of_circumflex_accents,
                number_of_ampersands, number_of_stars, number_of_parenthesis, number_of_minuses, number_of_underscores,
                number_of_equals, number_of_pluses, number_of_brackets, number_of_curly_brackets,
                number_of_vertical_bars, number_of_semicolons, number_of_colons, number_of_apostrophes,
                number_of_grave_accents, number_of_quotation_marks, number_of_slashes, number_of_less_grater_than_signs,
                number_of_words_in_bot_popular_words, number_of_words_in_human_popular_words,
                number_of_words_in_male_popular_words, number_of_words_in_female_popular_words,
                number_of_words_in_bot_human_popular_words, number_of_words_in_human_bot_popular_words,
                number_of_words_in_male_female_popular_words, number_of_words_in_female_male_popular_words,
                number_of_lines, number_of_words_per_line, number_of_money, number_of_words_start_with_capital_letter,
                number_of_free_words, number_of_political_words, longest_repeated_str_len,
                number_of_longest_repeated_str, longest_repeated_str_mix_feature, number_of_different_words]

    def number_of_syllables_per_tweet(self, tweet):
        number_of_syllables = 0

        for word in re.findall(r'\w+', tweet):
            number_of_syllables += self.syllables_dic.inserted(word).count('-')

        return number_of_syllables

    def number_of_words_in_bot_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_bot_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_bot_popular_words])

    def number_of_words_in_human_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_human_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_human_popular_words])

    def number_of_words_in_male_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_male_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_male_popular_words])

    def number_of_words_in_female_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_female_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_female_popular_words])

    def number_of_words_in_bot_human_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_bot_human_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_bot_human_popular_words])

    def number_of_words_in_human_bot_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_human_bot_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_human_bot_popular_words])

    def number_of_words_in_male_female_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_male_female_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_male_female_popular_words])

    def number_of_words_in_female_male_popular_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            return len([word for word in stemmed_words if word in self.en_female_male_popular_words])
        if self.language is 'es':
            return len([word for word in stemmed_words if word in self.es_female_male_popular_words])

    def different_words_per_tweet(self, different_words, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]
        different_words.update(set(stemmed_words))

        return different_words

    def number_of_free_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            stemmed_free_words = [self.stemmer.stem(word) for word in self.en_free_words]
            return len([word for word in stemmed_words if word in stemmed_free_words])
        if self.language is 'es':
            stemmed_free_words = [self.stemmer.stem(word) for word in self.es_free_words]
            return len([word for word in stemmed_words if word in stemmed_free_words])

    def number_of_political_words_per_tweet(self, tweet):
        stemmed_words = [self.stemmer.stem(str(word).lower()) for word in re.findall(r'\w+', tweet)]

        if self.language is 'en':
            stemmed_free_words = [self.stemmer.stem(str(word).lower()) for word in self.en_political_words]
            return len([word for word in stemmed_words if word in stemmed_free_words])
        if self.language is 'es':
            stemmed_free_words = [self.stemmer.stem(str(word).lower()) for word in self.es_political_words]
            return len([word for word in stemmed_words if word in stemmed_free_words])

    @staticmethod
    def number_of_words_per_tweet(tweet):
        return len(re.findall(r'\w+', tweet))

    @staticmethod
    def number_of_characters_per_tweet(tweet):
        return len(tweet)

    @staticmethod
    def average_word_len_per_tweet(tweet):
        words = re.findall(r'\w+', tweet)
        return sum(len(word) for word in words) / len(words) if len(words) > 0 else 0

    def number_of_stop_words_per_tweet(self, tweet):
        return len([word for word in re.findall(r'\w+', tweet) if word in self.stop_words])

    @staticmethod
    def number_of_tags_per_tweet(tweet):
        return len([word for word in tweet.split() if str(word).startswith('@')])

    @staticmethod
    def number_of_hash_tags_per_tweet(tweet):
        return len([word for word in tweet.split() if str(word).startswith('#')])

    @staticmethod
    def readability_level(average_number_of_words, average_number_of_syllables_per_word):
        return (0.39 * average_number_of_words) + (11.8 * average_number_of_syllables_per_word) - 15.59

    @staticmethod
    def number_of_digits_per_tweet(tweet):
        return sum([sum(c.isdigit() for c in word) for word in tweet.split()])

    @staticmethod
    def number_of_secure_links_per_tweet(tweet):
        return str(tweet).count('https')

    @staticmethod
    def number_of_unsecured_links_per_tweet(tweet):
        return str(tweet).count('http')

    @staticmethod
    def number_of_percent_per_tweet(tweet):
        return str(tweet).count('%')

    @staticmethod
    def number_of_exclamation_marks_per_tweet(tweet):
        return str(tweet).count('!')

    @staticmethod
    def number_of_question_marks_per_tweet(tweet):
        return str(tweet).count('?')

    @staticmethod
    def number_of_commas_per_tweet(tweet):
        return str(tweet).count(',')

    @staticmethod
    def number_of_points_per_tweet(tweet):
        return str(tweet).count('.')

    @staticmethod
    def number_of_emoji_per_tweet(tweet):
        return emoji.demojize(tweet).count(':') / 2

    @staticmethod
    def number_of_tilde_per_tweet(tweet):
        return str(tweet).count('~')

    @staticmethod
    def number_of_dollars_per_tweet(tweet):
        return str(tweet).count('$')

    @staticmethod
    def number_of_circumflex_accents_per_tweet(tweet):
        return str(tweet).count('^')

    @staticmethod
    def number_of_ampersands_per_tweet(tweet):
        return str(tweet).count('&')

    @staticmethod
    def number_of_stars_per_tweet(tweet):
        return str(tweet).count('*')

    @staticmethod
    def number_of_parenthesis_per_tweet(tweet):
        return str(tweet).count('(') + str(tweet).count(')')

    @staticmethod
    def number_of_minuses_per_tweet(tweet):
        return str(tweet).count('-')

    @staticmethod
    def number_of_underscores_per_tweet(tweet):
        return str(tweet).count('_')

    @staticmethod
    def number_of_equals_per_tweet(tweet):
        return str(tweet).count('=')

    @staticmethod
    def number_of_pluses_per_tweet(tweet):
        return str(tweet).count('+')

    @staticmethod
    def number_of_brackets_per_tweet(tweet):
        return str(tweet).count('[') + str(tweet).count(']')

    @staticmethod
    def number_of_curly_brackets_per_tweet(tweet):
        return str(tweet).count('{') + str(tweet).count('}')

    @staticmethod
    def number_of_vertical_bars_per_tweet(tweet):
        return str(tweet).count('|')

    @staticmethod
    def number_of_semicolons_per_tweet(tweet):
        return str(tweet).count(';')

    @staticmethod
    def number_of_colons_per_tweet(tweet):
        return str(tweet).count(':')

    @staticmethod
    def number_of_apostrophes_per_tweet(tweet):
        return str(tweet).count('\'')

    @staticmethod
    def number_of_grave_accents_per_tweet(tweet):
        return str(tweet).count('`')

    @staticmethod
    def number_of_quotation_marks_per_tweet(tweet):
        return str(tweet).count('\"')

    @staticmethod
    def number_of_slashes_per_tweet(tweet):
        return str(tweet).count('/') + str(tweet).count('\\')

    @staticmethod
    def number_of_less_grater_than_signs_per_tweet(tweet):
        return str(tweet).count('<') + str(tweet).count('>')

    @staticmethod
    def number_of_lines_per_tweet(tweet):
        return str(tweet).count('\n')

    @staticmethod
    def number_of_money_per_tweet(tweet):
        return str(tweet).count('$')

    @staticmethod
    def number_of_words_start_with_capital_letter_per_tweet(tweet):
        return len(re.findall(r"\b[A-Z]\S+", tweet))

    @staticmethod
    def longest_repeated_substring(tweets):
        # Returns the longest repeating non-overlapping
        # substring in str

        tweets = str(tweets).lower()

        n = len(tweets)
        lcs_re = [[0 for x in range(n + 1)] for y in range(n + 1)]

        res = ""  # To store result
        res_length = 0  # To store length of result

        # building table in bottom-up manner
        index = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):

                # (j-i) > LCSRe[i-1][j-1] to remove
                # overlapping
                if (tweets[i - 1] == tweets[j - 1] and
                        lcs_re[i - 1][j - 1] < (j - i)):
                    lcs_re[i][j] = lcs_re[i - 1][j - 1] + 1

                    # updating maximum length of the
                    # substring and updating the finishing
                    # index of the suffix
                    if lcs_re[i][j] > res_length:
                        res_length = lcs_re[i][j]
                        index = max(i, index)

                else:
                    lcs_re[i][j] = 0

        # If we have non-empty result, then insert
        # all characters from first character to
        # last character of string
        if res_length > 0:
            for i in range(index - res_length + 1,
                           index + 1):
                res = res + tweets[i - 1]

        return res
