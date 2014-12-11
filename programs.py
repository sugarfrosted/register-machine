# -*- coding: utf-8 -*-
from collections import defaultdict
def subtractor(R_0=0, R_1=1, R_2=2, shift=0, output = True):
    program = [["jump"  , R_1, {"□": 4, "a": 1}],
        ["append", R_0, "a"],
        ["remove", R_1, "a"],
        ["jump"  , R_0, {"□": 0, "a": 0,}],
        ["remove", R_2, "a"],
        ["jump"  , R_0, {"□": 4, "a": 4}]]
    if output:
        program.append(["print" , R_0, "nothing"])
    return program

def adder(R_0=0, R_1=1, R_2=2, shift=0, output = True):
    program = [["jump"  , R_1, {"□": 4, "a": 1}],
        ["append", R_0, "a"],
        ["remove", R_1, "a"],
        ["jump"  , R_0, {"□": 0, "a": 0,}],
        ["jump"  , R_2, {"□": 8, "a": 5}],
        ["append", R_0, "a"],
        ["remove", R_2, "a"],
        ["jump"  , R_0, {"□": 4, "a": 4}]]
    if output:
        program.append(["print" , R_0, "nothing"])
    return program

def cleanup(R, shift=0):
    program = []
    def building(key):
        2*alphabet.index(key)+1+shift if key in alphabet else None
    dict1 = defaultdict(building, {"□":len(alphabet)})
    def base(key):
        return shift
    for char in alphabet:
        program += ["remove", R, char]


    
                
            


#def transfer(R_Source, R_Target, R_workspace, alphabet, shift=0):
#    program = []
#    diction = {}
#    counter = shift
#    for letter in alphabet:
#        diction[letter] = counter
#        program += ["append", R_
#        counter += 2

    

# def LessThan(R_0=0, R_1=1, R_2=2, R_3=3, shift=0, output = True):
#     program = subtractor(R_3, R_1, R_2, shift)
#     length = len(program) + shift
# 
#     program += [
