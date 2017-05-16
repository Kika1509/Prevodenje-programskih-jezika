#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set

pp = pprint.PrettyPrinter(indent=4)

line = ""
output = []
SSPACE = " "

def space(level):
    return level*SSPACE

def error(line):
    print "err " + (line if len(line) else "kraj")

#first sub-program
def program(level):
    global line, output
    line = sys.stdin.readline().strip()
    tokens = line.split()
    if tokens[0] in ["IDN","KR_ZA",""]:
        output.append("<program>")
        lista_naredbi(level+1)
    else:
        error(line)
        sys.exit()

#second sub-lista naredbi
def lista_naredbi(level):
    global line, output
    output.append(space(level)+"<lista_naredbi>")
    tokens = line.split()
    znak = tokens[0] if len(tokens) else ""
    if znak in ["IDN","KR_ZA"]:
        naredba(level+1)
        #line = sys.stdin.readline().strip()
        lista_naredbi(level+1)
    elif znak in ["","KR_AZ"]:
        output.append(space(level+1)+"$")
    else:
        error(line)
        sys.exit()



#third sub-naredba
def naredba(level):
    global line, output
    tokens = line.split()
    output.append(space(level)+"<naredba>")
    if (tokens[0] == 'IDN'):
        naredba_pridruzivanja(level+1)
    elif tokens[0] == 'KR_ZA':
        za_petlja(level+1)
    else:
        error(line)
        sys.exit()

#fourth sub-naredba pridruživanja
def naredba_pridruzivanja(level):
    global line, output
    output.append(space(level)+"<naredba_pridruzivanja>")
    output.append(space(level+1)+line)
    line = sys.stdin.readline().strip()
    tokens = line.split()
    if tokens[0]== "OP_PRIDRUZI":
        output.append(space(level+1)+line)
        EE(level+1)
    else:
        error(line)
        sys.exit()

#fifth sub-za_petlja
def za_petlja(level):
    global line, output
    output.append(space(level)+"<za_petlja>")
    output.append(space(level+1)+line)
    line = sys.stdin.readline().strip()
    tokens = line.split()
    if tokens[0]== "IDN":
        output.append(space(level+1)+line)
    else:
        error(line)
        sys.exit()
    line = sys.stdin.readline().strip()
    tokens = line.split()
    if tokens[0]== "KR_OD":
        output.append(space(level+1)+line)
        EE(level+1)
        tokens = line.split()
        if tokens[0]=="KR_DO":
            output.append(space(level+1)+line)
            EE(level+1)
            lista_naredbi(level+1)
            tokens = line.split()
            if tokens[0]=="KR_AZ":
                output.append(space(level+1)+line)
                line = sys.stdin.readline().strip()
            else:
                print "err kraj"
                sys.exit()
        else:
            error(line)
            sys.exit()
    else:
        error(line)
        sys.exit()


#sixth sub-EE
def EE(level):
    global line, output
    output.append(space(level)+"<E>")
    line = sys.stdin.readline().strip()
    tokens = line.split()
    if len(line) and tokens[0] in ["IDN","BROJ","OP_PLUS","OP_MINUS","L_ZAGRADA"]:
        TT(level+1)
        EE_lista(level+1)
    else:
        error(line)
        sys.exit()

#seventh sub-E_lista
def EE_lista(level):
    global line, output
    output.append(space(level)+"<E_lista>")
    tokens = line.split()
    znak = tokens[0] if len(tokens) else ""
    if znak in ['OP_PLUS','OP_MINUS']:
        output.append(space(level+1)+line)
        EE(level+1)
    elif znak in ["IDN","KR_ZA","KR_DO","KR_AZ","D_ZAGRADA",""]:
        output.append(space(level+1)+"$")
    else:
        error(line)
        sys.exit()

#eighth sub-TT
def TT(level):
    global line, output
    output.append(space(level)+"<T>")
    #line = sys.stdin.readline().strip()
    tokens = line.split()
    if tokens[0] in ["IDN","BROJ","OP_PLUS","OP_MINUS","L_ZAGRADA"]:
        PPP(level+1)
        line = sys.stdin.readline().strip()
        TT_lista(level+1)
    else:
        error(line)
        sys.exit()


#nineth sub-TT_lista
def TT_lista(level):
    global line, output
    output.append(space(level)+"<T_lista>")
    tokens = line.split()
    znak = tokens[0] if len(tokens) else ""
    if znak in ['OP_PUTA','OP_DIJELI']:
        output.append(space(level+1)+line)
        line = sys.stdin.readline().strip()
        TT(level+1)
    elif znak in ["IDN","KR_ZA","KR_DO","KR_AZ","OP_PLUS","OP_MINUS","D_ZAGRADA",""]:
        output.append(space(level+1)+"$")
    else:
        error(line)
        sys.exit()

#tenth sub-PPP
def PPP(level):
    global line, output
    output.append(space(level)+"<P>")
    tokens = line.split()
    if tokens[0] in ["OP_PLUS","OP_MINUS"]:
        output.append(space(level+1)+line)
        line = sys.stdin.readline().strip()
        PPP(level+1)
    elif tokens[0] in ["L_ZAGRADA"]:
        output.append(space(level+1)+line)
        EE(level+1)
        tokens = line.split()
        if tokens[0]=="D_ZAGRADA":
            output.append(space(level+1)+line)
        else:
            error(line)
            sys.exit()
    elif tokens[0] in ["IDN","BROJ"]:
        output.append(space(level+1)+line)
    else:
        error(line)
        sys.exit()


#main program
#line = sys.stdin.readline()
#line = line.strip()
#line=line
program(0)
print "\n".join(output)

