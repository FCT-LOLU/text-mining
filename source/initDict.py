from metrics import *
from separator import *
import os


def init_dict_multiwords_expression(corpuspath):
    for i in range(1,9):
        bysize = {}
        ngrams[i] = bysize
    for file_name in os.listdir(corpuspath):
        file_path = os.path.join(corpuspath, file_name)
        if os.path.isfile(file_path):
            print(file_path)
            corpus_treatment(file_path)
            with open(file_path, 'r') as corpus:
                for line in corpus:
                    words = line.split()
                    for i in range(1,9):
                        for j in range(len(words)-i+1):
                            ngram = ' '.join(words[j:j+i])
                            if ngram not in ngrams[i]:
                                ngrams[i][ngram]={}
                                ngrams[i][ngram]["freq"] = 1
                                ngrams[i][ngram]["SCP"] = 0
                                ngrams[i][ngram]["MaxOmegaPlusSCP"] = 0
                                ngrams[i][ngram]["MaxOmegaMinusSCP"] = 0
                                ngrams[i][ngram]["Dice"]=0
                                ngrams[i][ngram]["MaxOmegaPlusDice"] = 0
                                ngrams[i][ngram]["MaxOmegaMinusDice"] = 0
                                ngrams[i][ngram]["MI"]=0
                                ngrams[i][ngram]["MaxOmegaPlusMI"] = 0
                                ngrams[i][ngram]["MaxOmegaMinusMI"] = 0
                            else:
                                ngrams[i][ngram]["freq"] += 1
                        
        
def fill_dict_multiwords_expression(number_words):
    for i in range(8,1,-1):
        print("size of n_grams: ",i)
        for ngram, value in ngrams[i].items():
            calculSCP(ngram,value)
            calculDice(ngram,value)
            calculMI(ngram,value,number_words)
            first_multiword_expression = ngram.split()[0:i-1]
            first_multiword_expression = ' '.join(first_multiword_expression)
            if(ngrams[i-1][first_multiword_expression]["SCP"] == 0):
                calculSCP(first_multiword_expression, ngrams[i-1][first_multiword_expression])
            if(ngrams[i-1][first_multiword_expression]["Dice"] == 0):
                calculDice(first_multiword_expression, ngrams[i-1][first_multiword_expression])
            if(ngrams[i-1][first_multiword_expression]["MI"] == 0):
                calculMI(first_multiword_expression, ngrams[i-1][first_multiword_expression],number_words)
            second_multiword_expression = ngram.split()[1:i]
            second_multiword_expression = ' '.join(second_multiword_expression)
            if(ngrams[i-1][second_multiword_expression]["SCP"] == 0):
                calculSCP(second_multiword_expression, ngrams[i-1][second_multiword_expression])
            if(ngrams[i-1][second_multiword_expression]["Dice"] == 0):
                calculDice(second_multiword_expression, ngrams[i-1][second_multiword_expression])
            if(ngrams[i-1][second_multiword_expression]["MI"] == 0):
                calculMI(second_multiword_expression, ngrams[i-1][second_multiword_expression],number_words)
            if(i!=2):
                ngrams[i-1][first_multiword_expression]["MaxOmegaPlusSCP"] = max(ngrams[i-1][first_multiword_expression]["MaxOmegaPlusSCP"],ngrams[i][ngram]["SCP"])
                ngrams[i-1][second_multiword_expression]["MaxOmegaPlusSCP"] = max(ngrams[i-1][second_multiword_expression]["MaxOmegaPlusSCP"],ngrams[i][ngram]["SCP"])
                ngrams[i-1][first_multiword_expression]["MaxOmegaPlusDice"] = max(ngrams[i-1][first_multiword_expression]["MaxOmegaPlusDice"],ngrams[i][ngram]["Dice"])
                ngrams[i-1][second_multiword_expression]["MaxOmegaPlusDice"] = max(ngrams[i-1][second_multiword_expression]["MaxOmegaPlusDice"],ngrams[i][ngram]["Dice"])
                ngrams[i-1][first_multiword_expression]["MaxOmegaPlusMI"] = max(ngrams[i-1][first_multiword_expression]["MaxOmegaPlusMI"],ngrams[i][ngram]["MI"])
                ngrams[i-1][second_multiword_expression]["MaxOmegaPlusMI"] = max(ngrams[i-1][second_multiword_expression]["MaxOmegaPlusMI"],ngrams[i][ngram]["MI"])
            if(i!=8):
                ngrams[i][ngram]["MaxOmegaMinusSCP"] = max(ngrams[i-1][first_multiword_expression]["SCP"],ngrams[i-1][second_multiword_expression]["SCP"])
                ngrams[i][ngram]["MaxOmegaMinusDice"] = max(ngrams[i-1][first_multiword_expression]["Dice"],ngrams[i-1][second_multiword_expression]["Dice"])
                ngrams[i][ngram]["MaxOmegaMinusMI"] = max(ngrams[i-1][first_multiword_expression]["MI"],ngrams[i-1][second_multiword_expression]["MI"])

def corpus_treatment(file_path):
    add_space_before_and_after_special_characters(file_path, [";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])
    modify_file_to_single_line(file_path, file_path)
