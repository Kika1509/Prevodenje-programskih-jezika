#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set

pp = pprint.PrettyPrinter(indent=4)

linija = []
prethodnalinija = []
red = []
znak = 0
razina = 0
indeks = 0
plparts = []
pridruzivanje = "OP_PRIDRUZI"

while(1):
    line = sys.stdin.readline().strip()
    if len(line)==0:
        sys.exit()
    tokens = line.split()
#print tokens
    if tokens[0] in ["IDN"]:
        if tokens[2] in linija and str(prethodnalinija) in "<naredba_pridruzivanja>":
            prethodnalinija = str(line)
            continue
        elif tokens[2] in linija:
            i=0
            while tokens[2] != linija[i]:
                i+=1
            znak = str(tokens[2])
            print str(razina)+" "+str(red[i])+" "+znak
            i=0
            prethodnalinija = line
        elif prethodnalinija.find("OP_PRIDRUZI") != -1 and tokens[2] not in linija:
            print "err "+str(razina)+znak
            sys.exit()
        elif tokens[2] not in linija:
            linija.append(tokens[2])
            #print linija
            red.append(tokens[1])
            prethodnalinija = line
    else:
        if line in "<lista_naredbi>":
            razina+=1
        prethodnalinija = line

