from initDict import *
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
    fill_dict_multiwords_expression()
    print("fill_dict_multiwords_expression done")
    data = ["p", "SCP", "Dice", "listSCP", "listDice"]
    with open('corpus2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        for p in range(2,6):
            print("p = ",p)
            print("SCP")
            SCP = localMaxSCP(p, stopwords_detected)
            lenSCP = len(SCP)
            print("Dice")
            Dice = localMaxDice(p, stopwords_detected)
            lenDice = len(Dice)
            data = [p, lenSCP, lenDice, SCP, Dice]
            writer.writerow(data)



def localMaxSCP(p, stopwords_detected):
    relevant_ngrams = []
    for i in range(2,8):
        for ngram, value in ngrams[i].items():
            words = ngram.split()
            if value['freq']>1 and words[0] not in stopwords_detected and words[-1] not in stopwords_detected:
                if(i==2):
                    if value['SCP']>= value['MaxOmegaPlusSCP']:
                        relevant_ngrams.append(ngram)
                else:
                    if value['SCP']>= pow(((pow(value['MaxOmegaPlusSCP'],p)+pow(value['MaxOmegaMinusSCP'],p))/2),(1/p)):
                        relevant_ngrams.append(ngram)
    return relevant_ngrams

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

    

def detect_stopwords_file(file_path, language_of_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = word_tokenize(content)

    stopwords_en = set(stopwords.words(language_of_file))

    stopwords_detected = list(set(word.lower() for word in words if word.lower() in stopwords_en))

    return stopwords_detected




beginning = time.time()
localMax("corpus2mw")
end = time.time()

print(end-beginning)