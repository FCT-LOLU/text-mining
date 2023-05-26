import csv
import sys
from separator import *

csv.field_size_limit(sys.maxsize)

def recall_dico():
    recall_dico={}
    add_space_before_and_after_special_characters("RE.txt",[";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])
    with open("RE.txt", 'r') as fichier:
        contenu = fichier.read()
        words = contenu.split('\n')
        with open("corpus2.csv", 'r') as file:
                csvreader = csv.reader(file, delimiter=',')
                for row in csvreader:
                    if row[0]!= 'p':
                        recall_dico[row[0]]={}
                        recall_dico[row[0]]['SCP']=recall_calcul(words,row[3])
                        recall_dico[row[0]]['Dice']=recall_calcul(words,row[4])
    return recall_dico
            


def recall_calcul(words,list):
    true_positive =0
    false_positive =0
    for word in words:
        if word in list:
            true_positive+=1
        else:
            false_positive+=1
    print(true_positive)
    return (true_positive/(true_positive+false_positive))*100

print(recall_dico())