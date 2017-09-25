# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 00:39:14 2017

@author: umang
"""

import sys
import os

def vr_debug(message, *values):
    vr_debugging = os.getenv("VR_DEBUG")
    if vr_debugging is None:
        # Debugging is off, do nothing.
        return
    if len(values) == 0:
        print (message),
    else:
        print (message, ":",) 
    #print "len(values):", len(values)
    for value in values:
        #print repr(value), " ",
        print (value),
    print

def main():
    # Test the vr_debug function with some calls.
    vr_debug('z') # Debug message without any associated values.
    # Debug messages with values:
    vr_debug('a', 1)
    vr_debug('b', 1, "hi")
    vr_debug('c', 1, "hi", True)
    vr_debug('d', 1, "hi", True, [2, 3])
    vr_debug('d', 1, "hi", True, [2, 3], {'a': 'apple', 'b': 'banana'})

if __name__ == '__main__':
    main()