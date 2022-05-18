from lib.reading import read_file
from lib.pre_parser import to_normal_view
from lib.post_parser import frame_creation

def to_pars(file_name, key_words_for_delete=["WEFAC"]):
    dirty_file = read_file(filename)
    clean_file = to_normal_view(dirty_file, key_words_for_delete)
    df_file = frame_creation(clean_file)
    return df_file

