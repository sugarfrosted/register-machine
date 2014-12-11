# -*- coding: utf-8 -*-
class Register:
    def __init__(self, start={}):
        self.contents = start

    def getlast(self, address):
        if address not in self.contents:
            self.contents[address] = ""
            return "□"
        else:
            return self.contents[address][-1]

    def append(self, address, character):
        if address in self.contents:
            self.contents[address] += character
        else:
            self.contents[address] = character

    def is_empty(self, address):
        return self.getlast(address) == "□"

    def remove(self, address, character):
        if address in self.contents:
            if self.contents[address].endswith(character):
                self.contents[address] = self.contents[address][:-1]
        else:
            self.contents[address] = ""

    def echo(self, address):
        if address not in self.contents:
            self.contents[address] = ""
            print("□")
        elif self.is_empty(address):
           print("□")
        else:
            print(self.contents[address])
# command address 

    def execute(self, L, command, address, argument):
        if command == "append":
            self.append(address, argument)
            return L + 1
        elif command == "remove":
            self.remove(address, argument)
            return L + 1
        elif command == "print":
            self.echo(address)
            return L + 1
        elif command == "jump":
            last = self.getlast(address)
            return argument[last]

#class Mapping
###############################################################################
# an element in list_of_values has the following form. The first entry is a   #
# value and the following list are the elements mapped to it in the           #
# dictionary                                                                  #
###############################################################################

alphabet = 'abc'

class Alphabet:
    def __init__(self, alphabet):
        self.alphabet = list(set(alphabet))

    def __setitem__(self, key, item): 
        self.alphabet[key] = item

    def __getitem__(self, key): 
        return self.alphabet[key]

    def __repr__(self): 
        return repr(self.alphabet)

    def __len__(self): 
        return len(self.alphabet)

    def __delitem__(self, key): 
        del self.alphabet[key]

    def keys(self): 
        return self.alphabet.keys()

    def values(self):
        return self.alphabet.values()

    def __cmp__(self, dict):
        return cmp(self.alphabet, dict)

    def __contains__(self, item):
        return item in self.alphabet

    def add(self, key, value):
        self.alphabet[key] = value
        self.alphabet = list(set(self.alphabet))


    def __iter__(self):
        return iter(self.alphabet)

    def __call__(self):
        return self.alphabet

    def __unicode__(self):
        return unicode(repr(self.alphabet))
