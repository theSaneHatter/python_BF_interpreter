#!/usr/bin/env python3
#finished(ish) 02:11, 4-13-2025
#This fella is a bf interpreter that can interpret bf
import numpy as np
from time import sleep

code = '+.>>++.'
code = '>++[<+++>-]<.' #6 0
code = '>++++++++(8)[<+++++++++(9)>-]<.' #h aka #48
code = '''
>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<+
+.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-
]<+.
>>>>>>>>>>>>>>,.
''' #hello world
#code = '+>]<.'
code = list(code)
memsize = 1000 # in bytes
mem = list([0]*memsize)

def eval_bf_1(code, mem):
    pointer = 0
    for char in code:
        if char == '>':
            pointer += 1
        if char == '<':
            pointer -=1
            if pointer < 0:
                print(f'\033[31mError: Pointer too low... Setting to 0\033[0m')
                pointer = 0
        if char == '+':
            mem[pointer] += 1
        if char == '-':
            mem[pointer] -= 1
        if char == '.':
            print(mem[pointer])
        return mem

def bf_b(m,p,pl,cd,o):
    p -=1
    if p < 0:
        print(f'\033[31mError: Pointer too low... Setting to 0\033[0m')
        p=0
    return m,p,pl+1,o
def bf_f(m,p,pl,cd,o):
    p+=1
    return m,p,pl+1,o
def bf_p(m,p,pl,cd,o):
    m[p] +=1
    return m,p,pl+1,o
def bf_m(m,p,pl,cd,o):
    m[p] -=1
    return m,p,pl+1,o
def bf_pr(m,p,pl,cd,o):
    output = int(m[p])
    output = chr(output)
    o = str(o)+str(output)
    print(output, end='')
    return m,p,pl+1,o
def bf_ob(m,p,pl,cd,o):
    return m,p,pl+1,o
def bf_cb(m,p,pl,cd,o):
    #print(f'@From bf_cb(): This function has been called. p,pl:{p,pl}<')
    if m[p] == 0:
        return m,p,pl+1,o
    target = cd[0:pl+1]
    #print(f'@From bf_cb(): target:>{target}<')
    level = 0
    movement = 0
    for char in target[::-1]:
        #print(f'@From bf_cd(): @for loop: char:>{char}<, movement:>{movement}<, level:>{level}<')
        if char == '[':
            level -=1
        elif char == ']':
            level +=1
        if level == 0:
            #print(f'@From bf_cd: level soccesfully broken! Movement:>{movement}, cd[p+movement]:>{cd[p+movement]}<, pl:{pl}, p+movement:>{p+movement}<')
            break
        movement -=1
    #print(f'@from bf_cd(): movement:>{movement}<, pl:>{pl}<')
    pl = pl+movement
    if pl <0:
        print(f'\033[31mError: u probably have an unmached bracket at charictor number >{pl-movement}<\033[0m')

    #print(f'@From bf_cb(): level:>{level}<, pl:>{pl}<, movement:>{movement}<')
    #print(f'@From bf_cb(): m[p]:>{m[p]}<, m,p,pl:>{m,p,pl}<')
    return m,p,pl,o
def bf_c(m,p,pl,cd,o):
    m[p] = int(ord(input('')))
    return m,p,pl+1,o
map = {'<':bf_b,
       '>':bf_f,
       '+':bf_p,
       '-':bf_m,
       '.':bf_pr,
       '[':bf_ob,
       ']':bf_cb,
       ',':bf_c
       }


def eval_bf_1(code, mem):
    pointer = 0
    for char in code:
        if char == '>':
            pointer += 1
        if char == '<':
            pointer -=1
            if pointer < 0:
                print(f'\033[31mError: Pointer too low... Setting to 0\033[0m')
                pointer = 0
        if char == '+':
            mem[pointer] += 1
        if char == '-':
            mem[pointer] -= 1
        if char == '.':
            print(mem[pointer])
        return mem

def eval_bf(code, memsize=1000):
    eval_output = ''
    code = list(code)
    mem = list([0]*memsize)

    map = {'<':bf_b,
           '>':bf_f,
           '+':bf_p,
           '-':bf_m,
           '.':bf_pr,
           '[':bf_ob,
           ']':bf_cb,
           ',':bf_c
        }

    allowed_chars = ['<','>','+','-','.',',','[',']']
    pointer = 0
    place = 0
    count = 0
    while place <= len(code)-1:
        char = code[place]
        if char not in allowed_chars:
            #print(f'@\033[32mWorning: encountered unknown char: >{char}<\033[0m')
            place +=1
            continue

        ##print(f'@char:>{char}<,pointer:>{pointer}<')
        mem,pointer,place,eval_output = map[char](mem,pointer,place,code,eval_output)
        count +=1
        ##print(f'@count (aka loop ittorations):>{count}<, place:>{place}<, mem[pointer]:>{mem[pointer]}<')
    return f'\nOutput:\n{eval_output}'
e = eval_bf(code)
print(e)
