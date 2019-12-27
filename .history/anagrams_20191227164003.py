#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.

"""
__author__ = "Imraj423"


import sys
from collections import defaultdict

def alphabetize(string):
    """ alphabetize
        Given a string, return a string that includes the same letters in
        alphabetical order.

        Example:

        >>> print alphabetize('cab')
        abc

    """
    anagrams = defaultdict(list)
    for word in words:
        anagrams[alphabetize(word)].append(word)
    return anagrams
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    anagrams = {
        alphabetize(word): [
            w for w in words
            if alphabetize(w) == alphabetize(word)]
        for word in words}
    return anagrams
print find_anagrams(['cat', 'dog', 'act'])

if __name__ == "__main__":
    # run find anagrams of first argument
    if len(sys.argv) < 2:
        print("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            print(find_anagrams(words))