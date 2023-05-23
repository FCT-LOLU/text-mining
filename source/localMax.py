from initDict import *
from utils import *
from separator import *
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time
import csv

nltk.download('stopwords')
nltk.download('punkt')

def localMax(path):
    p=2
    corpus_path = path
    corpus_path = corpus_treatment(corpus_path)
    language_of_file = "english"
    stopwords_detected = detect_stopwords_file(corpus_path, language_of_file)
    init_dict_multiwords_expression(corpus_path)
    fill_dict_multiwords_expression()
    data = ["p", "SCP", "Dice", "inDiceNotSCP", "inSCPNotDice"]
    with open('corpus2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        for p in range(2,8):
            print("p = ",p)
            print("SCP")
            SCP = localMaxSCP(p, stopwords_detected)
            lenSCP = len(SCP)
            print("Dice")
            Dice = localMaxDice(p, stopwords_detected)
            lenDice = len(Dice)
            inDiceNotSCP = []
            for expression in Dice:
                if expression not in SCP:
                    inDiceNotSCP.append(expression)
            inSCPNotDice = []
            for expression in SCP:
                if expression not in Dice:
                    inSCPNotDice.append(expression)
            data = [p, lenSCP, lenDice, len(inDiceNotSCP), len(inSCPNotDice)]
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

def corpus_treatment(corpus_path):
    add_space_before_and_after_special_characters(corpus_path, [";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])
    modify_file_to_single_line(corpus_path, "treated"+corpus_path)
    return "treated"+corpus_path

all_texts_in_one("corpus2mw")


beginning = time.time()
localMax("alltexts.txt")
end = time.time()

print(end-beginning)