
tokens=[';',':','!','?','<','>','&',')','(','[',']']

def SCP(word1,word2,filepath):
    num_word1=0
    num_word2=0
    num_word12=0

    words_table=[]
    with open(filepath,'r') as file:
        for line in file:
            for word in line.split():
                wordb= word.lower()
                characters=";,:!?.&()[]<>"
                for x in range(len(characters)):
                    wordb=wordb.replace(characters[x],"")
                words_table.append(wordb)

    for i in range(len(words_table)):
        if words_table[i]==word1:
            num_word1+=1
        elif words_table[i]==word2:
            num_word2+=1
    for j in range(len(words_table)):
        if j<len(words_table):
            if words_table[j]==word1 :
                if words_table[j+1]==word2:
                    num_word12+=1

    SCP_x_y= pow(num_word12,2)/(num_word1*num_word2)

    return SCP_x_y

print(SCP('the','sale','/home/lola/Documents/TelecomNancy/ERASMUS/DataMining/text-mining/corpus4mw/fil_1'))

def SCP_N(words,filepath):
    words_b=[]
    n=0

    for word in words.split():
        n+=1
        words_b.append(word)

    num_words =[0]*n
    words_table=[]

    with open(filepath,'r') as file:
        for line in file:
            for word in line.split():
                wordb= word.lower()
                characters=";,:!?.&()[]<>"
                for x in range(len(characters)):
                    wordb=wordb.replace(characters[x],"")
                words_table.append(wordb)

    for i in range(len(words_table)):
        for j in range(n):
            if words_table[i]==words_b[j]:
                num_words[j]+=1
    
    num_nwords=0
    transition=0

    for k in range(len(words_table)):
        while words_table[k]==words_b[transition]:
            if k<len(words_table)-1:
                if transition<len(words_b)-1:
                    transition+=1
                    k=k+1
                    if transition==n:
                        num_nwords+=1
        transition=0

    return num_nwords


print(SCP_N('that the state government','/home/lola/Documents/TelecomNancy/ERASMUS/DataMining/text-mining/corpus4mw/fil_1'))
        
