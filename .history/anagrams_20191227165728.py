#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Imraj423"


import sys


def alphabetize(string):
    anagrams = {}
    for word in words:
        w = alphabetize(word)
        if not w in anagrams:
            anagrams[w] = [word]
        else:
            anagrams[w].append(word)
    return anagrams
    

if __name__ == "__main__":
    # run find anagrams of first argument
    if len(sys.argv) < 2:
        print("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            print(find_anagrams(words))

