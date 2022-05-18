import re


def clear_of_rubbish(virgin_file):
    virgin_file_cleared = []
    for i in virgin_file:
        a = i.split('--')[0]
        a = re.sub('\t', ' ', a)
        a = re.sub('/', '', a)
        a = re.sub("'", '', a)

        a = a.strip()
        virgin_file_cleared.append(a)
    return virgin_file_cleared

def probels_clearing(virgin_file):
    virgin_file_cleared=clear_of_rubbish(virgin_file)
    virgin_file_cleared_of_empties=[]
    probels=[i*' ' for i in range(100)]
    for i in virgin_file_cleared:
        if i!='' and i not in probels:
            virgin_file_cleared_of_empties.append(i)
    return virgin_file_cleared_of_empties

def to_normal_view(virgin_file,key_words_for_delete=["WEFAC"],key_words=['DATES', 'WEFAC', 'COMPDAT', 'COMPDATL', 'END']):

    list_0 = clear_of_rubbish(virgin_file)
    list_1 = probels_clearing(list_0)
    list_data = []
    for index, elem in enumerate(list_1):
        f = re.findall(r'[0-9][0-9]\s[A-Z]+\s[0-9]{4}', elem)
        if f:
            list_data.append(index)
    for number in range(len(list_data) - 1):
        if list_data[number + 1] - list_data[number] == 1:
            list_1.insert(list_data[number + 1], 'DATES')

    init_key_words = key_words
    init_key_words_final = init_key_words[:]
    delete_key_word = key_words_for_delete

    for key_word in delete_key_word:
        init_key_words_final.remove(key_word)

    list_2 = list_1[:]
    indices = [i for i, x in enumerate(list_1) if x in delete_key_word]
    list_for_drop_main = []
    for index in indices:
        list_for_drop = []
        i = index
        while list_1[i] not in init_key_words_final:
            list_for_drop.append(i)
            list_for_drop_main.append(list_for_drop)
            new_list = [item for sublist in list_for_drop_main for item in sublist]
            new_list = sorted(list(set(new_list)))
            i += 1
    for index, elem in enumerate(new_list):
        list_2.pop(elem - index)

    list_2 = list_2[:list_2.index('END')]

    start_list = []
    init_key_words_final.remove('END')
    for start in init_key_words_final:
        start_list.append(list_1.index(start))
    start_index = min(start_list)

    list_3 = []
    indices = [i for i, x in enumerate(list_2) if x == 'DATES']
    indices.insert(0, start_index)
    indices.append(len(list_2))
    for index in range(len(indices) - 1):
        list_3.append(list_2[indices[index]:indices[index + 1]])
    return list_3