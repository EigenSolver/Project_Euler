# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 02:16:38 2017

@author: 84338
"""

global suffixes;
suffixes = ["", "thousand", "million", "billion"];
 
global ones;
ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
 
global after_ten;
after_ten = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
 
global tens;
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"];
 
#handles the nomenclature of a triplet
#number: the number in the string form, index: position of the triplet
def gimmeThemWords(number, index):
    length = len(number);
    
    if(length > 3):
        return False;
    
    #pads the number's string representation with 0s on the left
    number = number.zfill(3);
    string = "";
 
    hundreds_digit = ord(number[0]) - 48;
    tens_digit = ord(number[1]) - 48;
    ones_digit = ord(number[2]) - 48;
    
    string += "" if number[0] == '0' else ones[hundreds_digit];
    string += " hundred " if not string == "" else "";
    
    if(tens_digit > 1):
        string += 'and ' if hundreds_digit!=0 else ''
        string += tens[tens_digit - 2];
        string += " ";
        string += ones[ones_digit];
    
    elif(tens_digit == 1):
        string+='and ' if hundreds_digit!=0 else ''
        string += after_ten[(int(tens_digit + ones_digit) % 10) - 1];
        
    elif(tens_digit == 0):
        if hundreds_digit!=0 and ones_digit!=0:
            string+='and '
        string += ones[ones_digit];
        
    #counter check to determine the positional system
    if(string.endswith("zero")):
        string = string[:-len("zero")];
    
    else:
        string += " ";
     
    if(not len(string) == 0):    
        string += suffixes[index];
        
    return string;
    
def count_capital(string):
    return sum(map(len, (string.strip(' ')).split(' ')))

    
if __name__=='__main__':
    count=0
    test={}
    for i in range(1,1000):
        word=gimmeThemWords(str(i),0)
        test[word]=count_capital(word)
        count+=test[word]
    
    print(count+11)