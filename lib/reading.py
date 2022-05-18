def read_file(filename):
    with open(filename, encoding='UTF-8') as f:
        virgin_file = f.read().splitlines()
    return virgin_file
