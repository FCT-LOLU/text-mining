def print_dictio(dictio, level=0):
    for cle, value in dictio.items():
        if isinstance(value, dict):
            print('\t' * level + str(cle) + ':')
            print_dictio(value, level + 1)
        else:
            print('\t' * level + str(cle) + ': ' + str(value))

