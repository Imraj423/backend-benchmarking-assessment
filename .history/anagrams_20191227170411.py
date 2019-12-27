#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Imraj423"


import sys


def alphabetize(string):
     """ alphabetize
        Given a string, return a string that includes the same letters in
        alphabetical order.
        Example:
        >>> print alphabetize('cab')
        abc
    """
    return "".join(sorted(string.lower()))


def find_anagrams():
    anagrams = {}
    for word in words:
        w = alphabetize(word)
        if w in anagrams:
            anagrams[w].append(word)
        else:
            anagrams[w] = [word]
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

