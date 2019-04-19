import pandas as pd
import matplotlib.pyplot as plt

# txt file format [pgram, normalizare, kernelFunc, acc]
percent = '5'
filename = 'IMDB_Procent' + percent + '.txt'
function_name_to_replace = 'KernelFrom2Lists'
is_max = True

results = pd.read_csv(filename, sep=' ', header=None)

formatted_data = pd.DataFrame()
formatted_data['p_gram'] = results[0]
formatted_data['function'] = results[2].str.replace(function_name_to_replace, '')
formatted_data['acc'] = results[3]

mask = results[1] > 0
column_name = 'function'
formatted_data.loc[mask, column_name] = 'N' + formatted_data.loc[mask, column_name]

plt.figure()
mean_data_frame = formatted_data.groupby('function').mean().sort_values(by=['acc'], ascending=False)
mean_data_frame.loc[:, 'acc'].plot(legend=True, title='Mean acc by kernel on ' + percent + '% from data')

plt.figure()
max_data_frame = formatted_data.groupby('function').max().sort_values(by=['acc'], ascending=False)
max_data_frame.loc[:, 'acc'].plot(legend=True, title='Max acc by kernel on ' + percent + '% from data')

functions_to_keep_max = ['NK3RN3LSQRT', 'K3RN3LSqared', 'NIntersect', 'Intersect']
functions_to_keep_mean = ['NK3RN3LSQRT', 'K3RN3L', 'NIntersect', 'Intersect']

if is_max:
    mask_functions_to_keep = formatted_data['function'].isin(functions_to_keep_max)
else:
    mask_functions_to_keep = formatted_data['function'].isin(functions_to_keep_mean)

formatted_data = formatted_data[mask_functions_to_keep]

df = formatted_data.pivot(index='p_gram', columns='function', values='acc')
ax = df.plot(figsize=(15, 10), linewidth=3)
plt.xlabel("p_gram")
plt.ylabel("acc")
plt.title('Kernels acc per p_gram on ' + percent + '% from data - keep ' + ('max' if is_max else 'mean'))
plt.savefig(('max' if is_max else 'mean') + '-' + 'fig.jpg')
plt.show()
