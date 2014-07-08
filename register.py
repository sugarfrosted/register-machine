# -*- coding: utf-8 -*-
class Register:
    def __init__(self, start={}):
        self.contents = start

    def getlast(self, address):
        if address not in self.contents:
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
            if self.contents[address] == "":
                self.contents.pop(address)

    def echo(self, address):
        if address not in self.contents:
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

class Map:
    def __init__(self, default, list_of_values, alphabet):
        self.alphabet = set(alphabet)
        self.mappings = dict((k, default) for k in self.alphabet)
        for pair in list_of_values:
            for char in intersection(set(pair[1]), self.alphabet):
                self.mappings[char] = pair[0]

    def __setitem__(self, key, item): 
        self.mappings[key] = item
        self.alphabet.add[key]

    def __getitem__(self, key): 
        return self.mappings[key]

    def __repr__(self): 
        return repr(self.mappings)

    def __len__(self): 
        return len(self.mappings)

    def __delitem__(self, key): 
        del self.mappings[key]
        self.alphabet.remove(key)

    def keys(self): 
        return self.mappings.keys()

    def values(self):
        return self.mappings.values()

    def __cmp__(self, dict):
        return cmp(self.mappings, dict)

    def __contains__(self, item):
        return item in self.mappings

    def add(self, key, value):
        self.mappings[key] = value
        self.alphabet.add(key)

    def __iter__(self):
        return iter(self.mappings)

    def __call__(self):
        return self.mappings

    def __unicode__(self):
        return unicode(repr(self.mappings))
