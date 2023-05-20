from initDict import *
from utils import *
from separator import *
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time

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
    print(relevant_ngrams)

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

all_texts_in_one("corpus")


beginning = time.time()
localMax("alltexts.txt" )
end = time.time()

print(end-beginning)