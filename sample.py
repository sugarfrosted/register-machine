# -*- coding: utf-8 -*-
from register import Register
from programs import subtractor
from sys import argv

R_1 = argv[1]
R_2 = argv[2]

sample = Register({1:R_1, 2:R_2})
base = 4
program = subtractor() #R_0 = R_1 - R_2

pointer = 0
while pointer < len(program):
    pointer = sample.execute(pointer, program[pointer][0], program[pointer][1], program[pointer][2])
