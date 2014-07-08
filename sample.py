# -*- coding: utf-8 -*-
from register import Register
from sys import argv

R_1 = argv[1]
R_2 = argv[2]

sample = Register({1:R_1, 2:R_2})
base = 4
program = [#R_0 = R_1 - R_2
        ["jump"  , 1, {"□": 4, "a": 1}],
        ["append", 0, "a"],
        ["remove", 1, "a"],
        ["jump"  , 0, {"□": 0, "a": 0,}],
        ["jump"  , 2, {"□": 8, "a": 5}],
        ["remove", 0, "a"],
        ["remove", 2, "a"],
        ["jump"  , 0, {"□": 4, "a": 4}],
        ["print" , 0, "nothing"]]

pointer = 0

while pointer < len(program):
    pointer = sample.execute(pointer, program[pointer][0], program[pointer][1], program[pointer][2])
