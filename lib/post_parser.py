import pandas as pd
import numpy as np

def frame_creation(virgin_file):
    wow = to_normal_view(virgin_file)
    not_splitted_yet_data = []
    for i in wow:
        for j in i:
            if 'W' in j:
                not_splitted_yet_data.append(j)
    data_with_dates = []
    for i in not_splitted_yet_data:
        for j in wow:
            if i in j and 'DATES' in j:
                data_with_dates.append(str(j[1]).replace(" ", "") + ' ' + i)
            if i in j and 'DATES' not in j:
                data_with_dates.append('no_date ' + i)
    for i in wow:
        if 'DATES' in i and len(i) == 2:
            data_with_dates.append(str(i[1]).replace(' ', ''))
    splitted_data = []
    for i in data_with_dates:
        splitted_data.append(i.split())
    for i in splitted_data:
        if 'LGR1' not in i:
            i.insert(2, '')
    final_data = pd.DataFrame()
    for i in splitted_data:
        final_data = final_data.append([i])
    columns_name = [
        'Date',
        'Well name',
        'Local grid name',
        'I',
        'J',
        'K upper',
        'K lower',
        'Flag on connection',
        'Saturation table',
        'Transmissibility factor',
        'Well bore diameter',
        'Effective Kh',
        'Skin factor',
        'Press_eq_radius'
    ]
    final_data.columns = columns_name
    final_data['Date'] = final_data.apply(
        lambda x:
        np.NaN if x['Date'] == 'no_date'
        else x['Date'], axis=1)
    final_data['Well name'] = final_data.apply(
        lambda x:
        np.NaN if 'W' not in x['Well name']
        else x['Well name'], axis=1)
    final_data['Local grid name'] = final_data.apply(
        lambda x:
        np.NaN if 'none' == x['Local grid name']
        else x['Local grid name'], axis=1)
    final_data['Date'] = final_data.apply(
        lambda x:
        x['Date'][0:2] + ' ' + x['Date'][2:5] + ' ' + x['Date'][5:9] if type(x['Date']) == str
        else x['Date'], axis=1)