import os

def print_dictio(dictio, level=0):
    for cle, value in dictio.items():
        if isinstance(value, dict):
            print('\t' * level + str(cle) + ':')
            print_dictio(value, level + 1)
        else:
            print('\t' * level + str(cle) + ': ' + str(value))


def all_texts_in_one(dirpath):
    exit_file = "alltexts.txt"
    with open(exit_file, 'w') as exit:
        for nom_fichier in os.listdir(dirpath):
            chemin_fichier = os.path.join(dirpath, nom_fichier)
            with open(chemin_fichier, 'r') as fichier:
                contenu = fichier.read()
                exit.write(contenu)
                exit.write("\n")
