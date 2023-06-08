
#TF- IDF
from initDict import *
import os
import math
import operator
import sys
import re
import string

# n grams dictionary contraining all the ngrams of the corpus
# and by ngram the frequency by document
#ngrams[i][ngram]["freqByDoc"]={}
#the format of freqByDoc is:
#ngrams[i][ngram]["freqByDoc"][file_name]=the frequency of the ngram in the file_name

#function that calculates the tf the frequency of the ngram in the document on the total number of words in the document for
def calculTF(ngram, document_path, document_name):
    with open(document_path, 'r') as document:
        total_number_words = 0
        for line in document:
            total_number_words += len(line.split())
        return ngrams[len(ngram.split())][ngram]["freqByDoc"][document_name]/total_number_words

#function that calculates the idf the logarithm of the total number of documents on the number of documents containing the ngram
def calculIDF(ngram, corpus_path):
    #calcul the number of documents in the corpus
    number_documents = 0
    for file_name in os.listdir(corpus_path):
        number_documents += 1
    #calcul the number of documents containing the ngram aka the size of the dictionary freqByDoc
    number_documents_containing_ngram = len(ngrams[len(ngram.split())][ngram]["freqByDoc"])

    return math.log(number_documents/number_documents_containing_ngram)

#function that calculates the tf-idf the product of the tf and the idf
def calculTFIDF(ngram, document_path, corpus_path):
    return calculTF(ngram, corpus_path+"/"+document_path, document_path)*calculIDF(ngram, corpus_path)

#More TF-IDF is high, more the ngram is specific to the document
#function that calculates the 15 most specific ngrams of the document
#relevant_ngrams_scp_by_doc
def calcul15MostSpecificRelevantExpressionsWithSCP(document_name, corpus_path):
    dico_15_most_specific_ngrams = {}
    dico_15_most_specific_ngrams["min"]=0
    dico_15_most_specific_ngrams["list_15_most_specific_ngrams"]={}
    
    for re in relevant_ngrams_scp_by_doc[document_name]:
        tf_idf= calculTFIDF(re, document_name, corpus_path)
        if(len(dico_15_most_specific_ngrams["list_15_most_specific_ngrams"])<15):
            dico_15_most_specific_ngrams["list_15_most_specific_ngrams"][re]=tf_idf
            if(tf_idf<dico_15_most_specific_ngrams["min"]):
                dico_15_most_specific_ngrams["min"]=tf_idf
        else:
            if(tf_idf>dico_15_most_specific_ngrams["min"]):
                dico_15_most_specific_ngrams["list_15_most_specific_ngrams"][re]=tf_idf
                dico_15_most_specific_ngrams["min"]=min(dico_15_most_specific_ngrams["list_15_most_specific_ngrams"].values())
                for key, value in dico_15_most_specific_ngrams["list_15_most_specific_ngrams"].items():
                    if(value==dico_15_most_specific_ngrams["min"]):
                        del dico_15_most_specific_ngrams["list_15_most_specific_ngrams"][key]
                        break   
        dico_15_most_specific_ngrams["min"]=min(dico_15_most_specific_ngrams["list_15_most_specific_ngrams"].values())
    return dico_15_most_specific_ngrams["list_15_most_specific_ngrams"]

#function that open a corpus and for each document calculates the 15 most specific relevant expressions and write them in a csv  file
#the format of the csv file is:
#fileX:re1,re2,re3,...,re15
#fileY:re1,re2,re3,...,re15
#...
#the csv name is corpus_15_most_specific_relevant_expressions.csv
def calcul15MostSpecificRelevantExpressionsWithSCPOfADocumentInACorpus(corpus_path):
    with open("corpus_15_most_specific_relevant_expressions.csv", 'w') as csv_file:
        for file_name in os.listdir(corpus_path):
            csv_file.write(file_name+":")
            for re in calcul15MostSpecificRelevantExpressionsWithSCP(file_name, corpus_path):
                csv_file.write(re+",")
            csv_file.write("\n")

    
