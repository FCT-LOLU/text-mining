import csv
from separator import *

def recall_dico():
    recall_dico={}
    add_space_before_and_after_special_characters("RE.txt",[";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])
    with open("RE.txt", 'r') as fichier:
        contenu = fichier.read()
        words = contenu.split('\n')
        with open("corpus2.csv", 'r') as file:
                csvreader = csv.reader(file, delimiter=',')
                
            


def recall_calcul(words,list):

    true_positive =0
    false_positive =0
    for word in words:
        if word in list:
            true_positive+=1
        else:
            false_positive+=1

    return (true_positive/(true_positive+false_positive))*100

recall_dico