from lib.parser import to_pars

filename = 'input_data/test_schedule.inc'
if __name__ == '__main__':
    output_df = to_pars(filename, key_words_for_delete=["WEFAC"])
    output_df.to_excel('output_data/output_file.xlsx')