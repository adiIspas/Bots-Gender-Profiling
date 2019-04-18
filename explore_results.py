import pandas as pd
import matplotlib.pyplot as plt

# txt file format [pgram, normalizare, kernelFunc, acc]
filename = 'IMDB_Procent=1.txt'
function_name_to_replace = 'KernelFrom2Lists'
normalized_kernel = True

results = pd.read_csv(filename, sep=' ', header=None)

if normalized_kernel:
    mask = results[1] > 0
    results = results[mask]
else:
    mask = results[1] == 0
    results = results[mask]


formattedData = pd.DataFrame()
formattedData['p_gram'] = results[0]
formattedData['function'] = results[2].str.replace(function_name_to_replace, '')
formattedData['acc'] = results[3]

mask = results[1] > 0
column_name = 'function'
formattedData.loc[mask, column_name] = 'N' + formattedData.loc[mask, column_name]

df = formattedData.pivot(index='p_gram', columns='function', values='acc')
ax = df.plot(figsize=(15, 10), linewidth=3)
plt.xlabel("p_gram")
plt.ylabel("acc")
plt.title('Normalized kernels acc per p_gram' if normalized_kernel else 'Non normalized Kernels acc per p_gram')
plt.savefig('normalize-' + str(normalized_kernel).lower() + '-' + 'fig.jpg')
plt.show()
