# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:41:20 2017

@author: 84338
"""

with open("p022_names.txt") as f:
    for line in f:
        name_list=line.split(",")
        name_list=[string.strip('"') for string in name_list]
        break

name_list.sort()

def cal_score(string):
    
    def capitalOrder(char,upper=True):
        if not upper:
            char=char.upper()
        return ord(char)-64
    
    score=0
    for char in string:
        score+=capitalOrder(char)
    return score

if __name__=="__main__":
    score=0
    for i in range(len(name_list)):
        score+=(i+1)*(cal_score(name_list[i]))
    
    print(score)
