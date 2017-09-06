# -*- coding: utf-8 -*-

def word_value(string):
    '''
    give a word, map every character to its alphabetical order number,
    return the sum of the numbers
    '''
    string=string.upper()
    count=0
    for char in string:
        count+=(ord(char)-64)
    return count

triangles=set([n*(n+1)/2 for n in range(100)])

with open('p042_words.txt') as f:
    words=f.read().replace('"','').split(',')

count=0

for word in words:
    if word_value(word) in triangles:
        count+=1

print(count)