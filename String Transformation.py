#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    result = []
    result.append(sentence[0])
    for i in range(1,len(sentence)):
        if(sentence[i] != ' '):
            if sentence[i-1].lower() < sentence[i].lower() and sentence[i-1] !=' ':
                result.append(sentence[i].upper())
            elif sentence[i-1].lower() > sentence[i].lower() and sentence[i-1] !=' ':
                result.append(sentence[i].lower())
            elif sentence[i-1].lower() == sentence[i].lower() and sentence[i-1] !=' ':
                result.append(sentence[i])
            else:
                result.append(sentence[i])
        else:
            result.append(sentence[i])
            #result.append(sentence[i+1])
    makeitastring = ''.join(map(str, result))
    return makeitastring
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
