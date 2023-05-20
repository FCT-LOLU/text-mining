from math import log

ngrams = {}

def calculSCP(ngram, value):
    num_SCP=  pow(value["freq"],2)
    words = ngram.split()
    if(len(words)!=1):
        if(len(words)==2):
            deno_SCP = ngrams[1][words[0]]["freq"]*ngrams[1][words[1]]["freq"]
        else:    
            n=len(words)
            deno_SCP =0
            for i in range(1,n-1):
                word_one_to_i = ' '.join(words[0:i])
                size_word_one_to_i = len(word_one_to_i.split())
                word_i_plus_1_to_n = ' '.join(words[i+1:n])
                size_word_i_plus_1_to_n = len(word_i_plus_1_to_n.split())
                deno_SCP +=ngrams[size_word_one_to_i][word_one_to_i]["freq"]*ngrams[size_word_i_plus_1_to_n][word_i_plus_1_to_n]["freq"]
            deno_SCP=deno_SCP*(1/(n-1))
        value["SCP"] = round(num_SCP/deno_SCP,4)

def calculDice(ngram,value):

    num_Dice=  value["freq"]*2
    words = ngram.split()
    if(len(words)!=1):
        if(len(words)==2):
            deno_Dice = ngrams[1][words[0]]["freq"]*ngrams[1][words[1]]["freq"]
        else:    
            n=len(words)
            deno_Dice =1
            for i in range(1,n-1):
                word_one_to_i = ' '.join(words[0:i])
                size_word_one_to_i = len(word_one_to_i.split())
                word_i_plus_1_to_n = ' '.join(words[i+1:n])
                size_word_i_plus_1_to_n = len(word_i_plus_1_to_n.split())
                deno_Dice +=ngrams[size_word_one_to_i][word_one_to_i]["freq"]+ngrams[size_word_i_plus_1_to_n][word_i_plus_1_to_n]["freq"]
            deno_Dice=deno_Dice*(1/(n-1))
        value["Dice"] = round(num_Dice/deno_Dice,4)

def calculMI(ngram,value):
    num_MI= value["freq"]
    words = ngram.split()
    if(len(words)!=1):
        if(len(words)==2):
            deno_MI = ngrams[1][words[0]]["freq"]*ngrams[1][words[1]]["freq"]
        else:    
            n=len(words)
            deno_MI =0
            for i in range(1,n-1):
                word_one_to_i = ' '.join(words[0:i])
                size_word_one_to_i = len(word_one_to_i.split())
                word_i_plus_1_to_n = ' '.join(words[i+1:n])
                size_word_i_plus_1_to_n = len(word_i_plus_1_to_n.split())
                deno_MI +=ngrams[size_word_one_to_i][word_one_to_i]["freq"]*ngrams[size_word_i_plus_1_to_n][word_i_plus_1_to_n]["freq"]
            deno_MI=deno_MI*(1/(n-1))
        value["MI"] = round(log(num_MI/deno_MI),4)