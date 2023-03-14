from typing import *
from collections import defaultdict
from collections import Counter

class Vocab():

    def __init__(self,
                 counter: Counter = None,
                 specials: Optional[List] = None,
                 min_freq = 1,
                 itos: List = None):
        
        # if the itos is not None, it will be used to build the vocab
        if itos:
            
            # integer -> string
            self.itos = itos

            # string -> integer
            self.stoi = dict()

            # building the stoi dictonary from the itos list
            for i, w in enumerate(itos):
                self.stoi[w] = i

        else:

            # integer -> string
            self.itos = list()

            # string -> integer
            # 1 corresponds to the unknown token string
            self.stoi = defaultdict(lambda: 1)

            i = 0

            # the specials token (pad, unk) are the ones with the smallest integer
            if specials is not None:
                for special in specials:
                    self.stoi[special] = i
                    i += 1

            # building the stoi dictionary from the counter of the occurences of the strings
            for occ in counter:
                freq = counter[occ]
                if freq >= min_freq:
                    self.stoi[occ] = i
                    i += 1

            # building the itos list from the stoi dictionary
            for w in self.stoi:
                self.itos.append(w)