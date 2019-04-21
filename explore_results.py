import pandas as pd
import matplotlib.pyplot as plt

# txt file format [pgram, normalizare, kernelFunc, acc]
percent = '1'
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
_, axes = plt.subplots(figsize=(18, 7))
plt.title('Mean acc by kernel on ' + percent + '% from IMDb data')
axes.plot(mean_data_frame['acc'])
plt.savefig('mean-acc-percent' + percent + '.png')


plt.figure()
max_data_frame = formatted_data.groupby('function').max().sort_values(by=['acc'], ascending=False)
_, axes = plt.subplots(figsize=(18, 7))
plt.title('Max acc by kernel on ' + percent + '% from IMDb data')
axes.plot(max_data_frame['acc'])
plt.savefig('max-acc-percent' + percent + '.png')

# 1%
functions_to_keep_max = ['NIntersect', 'Presence', 'K3RN3LSQRT', 'NK3RN3LSQRT']
functions_to_keep_mean = ['NIntersect', 'Spectrum', 'NK3RN3L', 'K3RN3LSQRT']

# 5%
# functions_to_keep_max = ['NK3RN3LSQRT', 'K3RN3LSqared', 'NIntersect', 'Intersect']
# functions_to_keep_mean = ['NK3RN3LSQRT', 'K3RN3L', 'NIntersect', 'Intersect']

if is_max:
    mask_functions_to_keep = formatted_data['function'].isin(functions_to_keep_max)
else:
    mask_functions_to_keep = formatted_data['function'].isin(functions_to_keep_mean)

formatted_data = formatted_data[mask_functions_to_keep]

df = formatted_data.pivot(index='p_gram', columns='function', values='acc')
ax = df.plot(figsize=(10, 7), linewidth=3)
plt.xlabel("p_gram")
plt.ylabel("acc")
plt.title('Kernels acc per p_gram on ' + percent + '% from IMDb data - based on ' + ('max' if is_max else 'mean') + ' acc')
plt.savefig(('max' if is_max else 'mean') + '-percent' + percent + '.jpg')
plt.show()

# load all data
percents = ['1', '5', '10', '15', '20']
normalize = False
if normalize:
    functions_to_keep = ['NK3RN3L', 'NIntersect', 'NPresence', 'NSpectrum']
else:
    functions_to_keep = ['K3RN3L', 'Intersect', 'Presence', 'Spectrum']

evolution_of_data = pd.DataFrame()

for percent in percents:
    filename = 'IMDB_Procent' + percent + '.txt'
    results = pd.read_csv(filename, sep=' ', header=None)

    over_time_formatted_data = pd.DataFrame()
    over_time_formatted_data['p_gram'] = results[0]
    over_time_formatted_data['function'] = results[2].str.replace(function_name_to_replace, '')
    over_time_formatted_data['acc'] = results[3]

    mask = results[1] > 0
    over_time_formatted_data.loc[mask, column_name] = 'N' + over_time_formatted_data.loc[mask, column_name]

    for function in functions_to_keep:
        temp = pd.DataFrame()
        mask_functions_to_keep = over_time_formatted_data['function'].isin([function])
        temp = over_time_formatted_data[mask_functions_to_keep]
        index = temp['acc'].argmax()
        acc = temp['acc'][index]

        temp_data = pd.DataFrame({'percent': [int(percent)], 'function': [function], 'acc': [acc]})
        evolution_of_data = evolution_of_data.append(temp_data)

final_data = evolution_of_data.pivot(index='percent', columns='function', values='acc')
ax = final_data.plot(figsize=(10, 7), linewidth=3)
plt.xlabel("percent")
plt.ylabel("acc")
plt.title('Kernels acc per percent of data based on max acc')
plt.savefig('evolution-of-data' + ('-normalize' if normalize else '') + '.jpg')
plt.show()
