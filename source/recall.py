import csv
import sys
from separator import *
from utils import print_dictio
from math import sqrt

csv.field_size_limit(sys.maxsize)

def metrics(precision, corpus_path,file_re):
    metrics_dico={}
    add_space_before_and_after_special_characters(file_re,[";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])
    with open(file_re, 'r') as fichier:
        contenu = fichier.read()
        words = contenu.split('\n')
        with open(corpus_path, 'r') as file:
                recall_dico ={}
                precision_dico={}
                f_metric_dico={}
                CI_dico={}
                csvreader = csv.reader(file, delimiter=',')
                for row in csvreader:
                    if row[0]!= 'p':
                        recall_dico[row[0]]={}
                        precision_dico[row[0]]={}
                        f_metric_dico[row[0]]={}
                        CI_dico[row[0]]={}
                        print(row[1])

                        CI_dico[row[0]]['SCP']={}
                        recall_dico[row[0]]['SCP']=recall_calcul(words,row[4])
                        precision_dico[row[0]]['SCP']= precision[0]
                        f_metric_dico[row[0]]['SCP']= ((2*precision_dico[row[0]]['SCP']*recall_dico[row[0]]['SCP'])/(precision_dico[row[0]]['SCP']+recall_dico[row[0]]['SCP']))
                        CI_dico[row[0]]['SCP']['Recall']=confidenceinterval(recall_dico[row[0]]['SCP']/100)
                        CI_dico[row[0]]['SCP']['Precision']=confidenceinterval(precision_dico[row[0]]['SCP']/100)
                        CI_dico[row[0]]['SCP']['F Metric']=confidenceinterval(f_metric_dico[row[0]]['SCP']/100)

                        CI_dico[row[0]]['Dice']={}
                        recall_dico[row[0]]['Dice']=recall_calcul(words,row[5])
                        precision_dico[row[0]]['Dice']= precision[1]
                        f_metric_dico[row[0]]['Dice']= ((2*precision_dico[row[0]]['Dice']*recall_dico[row[0]]['Dice'])/(precision_dico[row[0]]['Dice']+recall_dico[row[0]]['Dice']))
                        CI_dico[row[0]]['Dice']['Recall']=confidenceinterval(recall_dico[row[0]]['Dice']/100)
                        CI_dico[row[0]]['Dice']['Precision']=confidenceinterval(precision_dico[row[0]]['Dice']/100)
                        CI_dico[row[0]]['Dice']['F Metric']=confidenceinterval(f_metric_dico[row[0]]['Dice']/100)
                        
                        CI_dico[row[0]]['MI']={}
                        recall_dico[row[0]]['MI']=recall_calcul(words,row[6])
                        precision_dico[row[0]]['MI']= precision[2]
                        f_metric_dico[row[0]]['MI']= ((2*precision_dico[row[0]]['MI']*recall_dico[row[0]]['MI'])/(precision_dico[row[0]]['MI']+recall_dico[row[0]]['MI']))
                        CI_dico[row[0]]['MI']['Recall']=confidenceinterval(recall_dico[row[0]]['MI']/100)
                        CI_dico[row[0]]['MI']['Precision']=confidenceinterval(precision_dico[row[0]]['MI']/100)
                        CI_dico[row[0]]['MI']['F Metric']=confidenceinterval(f_metric_dico[row[0]]['MI']/100)
                        
                metrics_dico['Recall']= recall_dico
                metrics_dico['Precision']= precision_dico
                metrics_dico['F Metric']= f_metric_dico
                metrics_dico['Confidence Interval']=CI_dico
    

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

def confidenceinterval(value):
    interval= 1.96*sqrt(value*(1-value)/200)
    CI=[value-interval,value+interval]
    return CI


print_dictio(metrics([72,74,65.5],"corpus2.csv","RE.txt"))
print_dictio(metrics([68.5,88,80],"frenchcorpus.csv","FrenchRecall.txt"))



