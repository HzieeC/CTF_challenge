#!/usr/bin/python
# -*- coding: UTF-8 -*-
a ="1011 11111 001 01 010 0 00001 111 110 11111 111 100 1001 110 00001 1 0010 00011 010"
a2=""
for i in a:
    if i=="0":
        a2+="."
    elif i=="1":
        a2+="-"
    else:
        a2+=" "
print(a2)

s = a2.split(" ")
print(len(s))
dict = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---':'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.'
        };
for item in s:
    print (dict[item],end='')

