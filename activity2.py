def match(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr=ctr+1
            list.append(word)
    print("List of words with first and last charecters same:",list)
    return ctr
count=match(["abc","cfc","bgb","lopal","bwidjb","tota"])
print("number of words having first and last charecter same:",count)