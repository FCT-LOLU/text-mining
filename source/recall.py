import csv
import sys
from separator import *
from utils import print_dictio

csv.field_size_limit(sys.maxsize)

def metrics(precision, corpus_path,file_re):
    metrics_dico={}
    add_space_before_and_after_special_characters("RE.txt",[";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])
    with open(file_re, 'r') as fichier:
        contenu = fichier.read()
        words = contenu.split('\n')
        with open(corpus_path, 'r') as file:
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
                        recall_dico[row[0]]['SCP']=recall_calcul(words,row[4])
                        precision_dico[row[0]]['SCP']= precision[0]
                        f_metric_dico[row[0]]['SCP']= ((2*precision_dico[row[0]]['SCP']*recall_dico[row[0]]['SCP'])/(precision_dico[row[0]]['SCP']+recall_dico[row[0]]['SCP']))
                        recall_dico[row[0]]['Dice']=recall_calcul(words,row[5])
                        precision_dico[row[0]]['Dice']= precision[1]
                        f_metric_dico[row[0]]['Dice']= ((2*precision_dico[row[0]]['Dice']*recall_dico[row[0]]['Dice'])/(precision_dico[row[0]]['Dice']+recall_dico[row[0]]['Dice']))
                        recall_dico[row[0]]['MI']=recall_calcul(words,row[6])
                        precision_dico[row[0]]['MI']= precision[2]
                        f_metric_dico[row[0]]['MI']= ((2*precision_dico[row[0]]['MI']*recall_dico[row[0]]['MI'])/(precision_dico[row[0]]['MI']+recall_dico[row[0]]['MI']))
                        
                        
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

print_dictio(metrics([72,74,65.5],"corpus2.csv","RE.txt"))
print_dictio(metrics([68.5,0,0],"frenchcorpus.csv","FrenchRecall.txt"))



