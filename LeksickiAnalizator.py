# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set


az = "az"
za= "za"
od= "od"
do = "do"
key_words = []
key_words.append(za)
key_words.append(od)
key_words.append(do)
key_words.append(az)
red = 1
arg = []
num = []


not_a_letter = []
not_a_letter.append("=")
not_a_letter.append("+")
not_a_letter.append("-")
not_a_letter.append("/")
not_a_letter.append("*")
not_a_letter.append("(")
not_a_letter.append(")")


def slovo(sign):
    arg.append(sign)

def zadnje_slovo(sign):
    arg.append(sign)
    print ("IDN"+' '+str(red)+' '+''.join(arg))

def znak(sign, next_sign):
    if (sign == '=' ):
        print ("OP_PRIDRUZI"+' '+str(red)+' '+sign)
    elif (sign == "+"):
        print ("OP_PLUS"+' '+str(red)+' '+sign)
    elif (sign == "-"):
        print ("OP_MINUS"+' '+str(red)+' '+sign)
    elif (sign == "*"):
        print ("OP_PUTA"+' '+str(red)+' '+sign)
    elif (sign == "("):
        print ("L_ZAGRADA"+' '+str(red)+' '+sign)
    elif (sign == ")"):
        print ("D_ZAGRADA"+' '+str(red)+' '+sign)
    elif (sign == '/'):
        if (next_sign == '/'):
            return False
        else:
            print ("OP_DIJELI"+' '+str(red)+' '+sign)



def kljucna_rijec(part):
    if (part == "za"):
        print ("KR_ZA"+' '+str(red)+' '+part)
    elif (part == "od"):
        print ("KR_OD"+' '+str(red)+' '+part)
    elif (part == "do"):
        print ("KR_DO"+' '+str(red)+' '+part)
    elif (part == "az"):
        print ("KR_AZ"+' '+str(red)+' '+part)


def zadnji_znak(sign):
    if (sign == "="):
        print ("OP_PRIDRUZI"+' '+str(red)+' '+sign)
    elif (sign == "+"):
        print ("OP_PLUS"+' '+str(red)+' '+sign)
    elif (sign == "-"):
        print ("OP_MINUS"+' '+str(red)+' '+sign)
    elif (sign == "*"):
        print ("OP_PUTA"+' '+str(red)+' '+sign)
    elif (sign == "("):
        print ("L_ZAGRADA"+' '+str(red)+' '+sign)
    elif (sign == ")"):
        print ("D_ZAGRADA"+' '+str(red)+' '+sign)
    elif (sign == "/"):
        print ("OP_DIJELI"+' '+str(red)+' '+sign)



def broj(number):
    num.append(number)


def zadnji_broj(number):
    num.append(number)
    print ("BROJ"+' '+str(red)+' '+''.join(num))

while 1:
    prekid=0
    line = sys.stdin.readline()
    if not line:
        break
    line = line.strip()
    content = line.split(" ")
    for part in content:
        i=0
        separated_content = list(part)
        if (part in key_words):
            kljucna_rijec(part)
        else:
            while (i < len(separated_content) and (prekid == 0)):
                if (ord(separated_content[i]) in range(65,91) or ord(separated_content[i]) in range(97,123)):
                    while ((i < len(separated_content)-1) and separated_content[i] not in not_a_letter):
                        slovo(separated_content[i])
                        i+=1
                    if (i == len(separated_content)-1):
                        zadnje_slovo(separated_content[i])
                        arg[:] = []
                        break
                    else:
                        print ("IDN"+' '+str(red)+' '+''.join(arg))
                        arg[:] = []
                        if (znak(separated_content[i],separated_content[i+1]) == False):
                            #i = len(separated_content)
                            prekid = 1
                            break
                        else:
                            i+=1
                elif ord(separated_content[i]) in range(48,58):
                    if (i == len(separated_content)-1):
                        zadnji_broj(separated_content[i])
                        num[:] = []
                        break
                    elif (ord(separated_content[i+1]) in range(48,58)):
                        broj(separated_content[i])
                        i+=1
                    else:
                        zadnji_broj(separated_content[i])
                        num[:] = []
                        i+=1
                else:
                    if (i == len(separated_content)-1):
                        zadnji_znak(separated_content[i])
                        break
                    elif (ord(separated_content[i+1]) not in range(65,91) and ord(separated_content[i+1]) not in range(97,123) and ord(separated_content[i+1]) not in range(48,58)):
                        if (znak(separated_content[i],separated_content[i+1]) == False):
                            #i = len(separated_content) + 1
                            prekid = 1
                            break
                        else:
                            i+=1
                    else:
                        zadnji_znak(separated_content[i])
                        i+=1



    red = red + 1


