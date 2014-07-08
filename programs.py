# -*- coding: utf-8 -*-
def subtractor(R_0=0, R_1=1, R_2=2, shift=0, output = True):
    program = [["jump"  , R_1, {"□": 4, "a": 1}],
        ["append", R_0, "a"],
        ["remove", R_1, "a"],
        ["jump"  , R_0, {"□": 0, "a": 0,}],
        ["jump"  , R_2, {"□": 8, "a": 5}],
        ["remove", R_0, "a"],
        ["remove", R_2, "a"],
        ["jump"  , R_0, {"□": 4, "a": 4}]]
    if output:
        program.append(["print" , R_0, "nothing"])
    return program
