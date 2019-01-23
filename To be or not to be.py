import os

toBeWords = ['am','are','were','was','is','been','being','be']
N = int(input())
text = input().lower().replace(".", "").replace(",", "")
wordList = text.split(" ")
n = 0
qf = 0

#Rule based checking for the values
for i in range(len(wordList)):
    if wordList[i] == "----":
        n += 1
        try:
            if n > N : break
            if wordList[i-1] in ['may', "can't", "can", "not", "will", 'might', 'would'] : print "be"; continue
            if wordList[i-1] in ['has', "had", "have"] : print "been"; continue
            if wordList[i-1] == 'which' and wordList[i-2][-1] == 's': print "were"; continue
            if wordList[i-1] in ['i'] : print "am"; continue
            if wordList[i-1][-1] == 's': print "were"; continue
            if wordList[i+1][-1] == 's': print "were"; continue
            if wordList[i+1][-2:] == 'ed' and ("if" in wordList[i-3:i] or "its" in wordList[i-3:i] or "a" in wordList[i:i+5]) : print "is"; continue
            if wordList[i-1] in ['which', 'it', 'he', 'that'] : print "was"; continue
            if wordList[i+1][-2:] == 'ed' and "a" in wordList[i:i+5]: print "been"; continue
            if wordList[i+1][-2:] == 'ed': print "was"; continue
            if wordList[i+2] == 'by': print "was"; continue
            if wordList[i+3] == 'by': print "was"; continue
            if wordList[i+1][-3:] == 'ing': print "were"; continue
            if "are" in wordList[i:i+5]: print "are"; continue
            if "were" in wordList[i:i+5]: print "were"; continue
            else: print "is"
        except:
            print "is"
        
