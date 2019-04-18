import pandas as pd
import matplotlib.pyplot as plt

# txt file format [pgram, normalizare, kernelFunc, acc]
filename = 'IMDB_Procent=1.txt'
results = pd.read_csv(filename, sep=' ', header=None)

formattedData = pd.DataFrame()
formattedData['p_gram'] = results[0]
formattedData['function'] = results[1].map(str) + '-' + results[2]
formattedData['acc'] = results[3]

df = formattedData.pivot(index='p_gram', columns='function', values='acc')
df.plot()
plt.savefig('fig.jpg')
plt.show()
