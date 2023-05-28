import csv
import sys
from separator import *
from utils import print_dictio

csv.field_size_limit(sys.maxsize)

def metrics():
    metrics_dico={}
    add_space_before_and_after_special_characters("RE.txt",[";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])
    with open("RE.txt", 'r') as fichier:
        contenu = fichier.read()
        words = contenu.split('\n')
        with open("corpus2.csv", 'r') as file:
                recall_dico ={}
                precision_dico={}
                f_metric_dico={}
                csvreader = csv.reader(file, delimiter=',')
                for row in csvreader:
                    if row[0]!= 'p':
                        recall_dico[row[0]]={}
                        precision_dico[row[0]]={}
                        f_metric_dico[row[0]]={}
                        print(row[2])
                        recall_dico[row[0]]['SCP']=recall_calcul(words,row[3])
                        precision_dico[row[0]]['SCP']= 72
                        f_metric_dico[row[0]]['SCP']= ((2*precision_dico[row[0]]['SCP']*recall_dico[row[0]]['SCP'])/(precision_dico[row[0]]['SCP']+recall_dico[row[0]]['SCP']))
                        recall_dico[row[0]]['Dice']=recall_calcul(words,row[4])
                        precision_dico[row[0]]['Dice']= 72
                        f_metric_dico[row[0]]['Dice']= ((2*precision_dico[row[0]]['Dice']*recall_dico[row[0]]['Dice'])/(precision_dico[row[0]]['Dice']+recall_dico[row[0]]['Dice']))
                        
                metrics_dico['Recall']= recall_dico
                metrics_dico['Precision']= precision_dico
                metrics_dico['F Metric']= f_metric_dico
    

    return metrics_dico
            


def recall_calcul(words,list):
    true_positive =0
    false_positive =0
    for word in words:
        if word in list:
            true_positive+=1
        else:
            false_positive+=1
    
    return (true_positive/(true_positive+false_positive))*100

print_dictio(metrics())

