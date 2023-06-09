from tfIdf import *
from utils import *
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time
import csv

nltk.download('stopwords')
nltk.download('punkt')

def localMax(corpus_path):
    all_texts_in_one(corpus_path)
    language_of_file = "english"
    corpus_treatment("alltexts.txt")
    stopwords_detected = detect_stopwords_file("alltexts.txt", language_of_file)
    print("stopwords_detected done")
    init_dict_multiwords_expression(corpus_path)
    print("init_dict_multiwords_expression done")
    number_words= how_many_words_in_file("alltexts.txt")
    fill_dict_multiwords_expression(number_words)
    print("fill_dict_multiwords_expression done")
    data = ["p", "SCP", "Dice", "MI","listSCP", "listDice","listMI"]
    with open('corpus2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        for p in range(2,6):
            print("p = ",p)
            print("SCP")
            localMaxSCP(p, stopwords_detected)
            lenSCP = len(relevant_ngrams_scp)
            print("Dice")
            Dice = localMaxDice(p, stopwords_detected)
            lenDice = len(Dice)
            print("MI")
            MI= localMaxMI(p,stopwords_detected)
            lenMI=len(MI)
            data = [p, lenSCP, lenDice,lenMI, relevant_ngrams_scp, Dice, MI]
            writer.writerow(data)
        f.close()
    calcul15MostSpecificRelevantExpressionsWithSCPOfADocumentInACorpus(corpus_path)
    



def localMaxSCP(p, stopwords_detected):
    for i in range(2,8):
        for ngram, value in ngrams[i].items():
            words = ngram.split()
            if value['freq']>1 and words[0] not in stopwords_detected and words[-1] not in stopwords_detected:
                if(i==2):
                    if value['SCP']>= value['MaxOmegaPlusSCP']:
                        relevant_ngrams_scp.append(ngram)
                        for doc, value in ngrams[i][ngram]["freqByDoc"].items():
                            if doc not in relevant_ngrams_scp_by_doc:
                                relevant_ngrams_scp_by_doc[doc] = []
                            relevant_ngrams_scp_by_doc[doc].append(ngram)
                else:
                    if value['SCP']>= pow(((pow(value['MaxOmegaPlusSCP'],p)+pow(value['MaxOmegaMinusSCP'],p))/2),(1/p)):
                        relevant_ngrams_scp.append(ngram)
                        for doc, value in ngrams[i][ngram]["freqByDoc"].items():
                            if doc not in relevant_ngrams_scp_by_doc:
                                relevant_ngrams_scp_by_doc[doc] = []
                            relevant_ngrams_scp_by_doc[doc].append(ngram)

def localMaxDice(p, stopwords_detected):
    relevant_ngrams = []
    for i in range(2,8):
        for ngram, value in ngrams[i].items():
            words = ngram.split()
            if value['freq']>1 and words[0] not in stopwords_detected and words[-1] not in stopwords_detected:
                if(i==2):
                    if value['Dice']>= value['MaxOmegaPlusDice']:
                        relevant_ngrams.append(ngram)
                else:
                    if value['Dice']>= pow(((pow(value['MaxOmegaPlusDice'],p)+pow(value['MaxOmegaMinusDice'],p))/2),(1/p)):
                        relevant_ngrams.append(ngram)
    return relevant_ngrams

def localMaxMI(p, stopwords_detected):
    relevant_ngrams = []
    for i in range(2,8):
        for ngram, value in ngrams[i].items():
            words = ngram.split()
            if value['freq']>1 and words[0] not in stopwords_detected and words[-1] not in stopwords_detected:
                if(i==2):
                    if value['MI']>= value['MaxOmegaPlusMI']:
                        relevant_ngrams.append(ngram)
                else:
                    if value['MI']>= pow(((pow(value['MaxOmegaPlusMI'],p)+pow(value['MaxOmegaMinusMI'],p))/2),(1/p)):
                        relevant_ngrams.append(ngram)
    return relevant_ngrams

    

def detect_stopwords_file(file_path, language_of_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = word_tokenize(content)

    stopwords_en = set(stopwords.words(language_of_file))

    stopwords_detected = list(set(word.lower() for word in words if word.lower() in stopwords_en))

    return stopwords_detected




beginning = time.time()
localMax("corpus2mw") # you can change here "corpus2mw" by "frenchCorpus" to run the algorithm on a fren corpus
end = time.time()
print(end-beginning)
