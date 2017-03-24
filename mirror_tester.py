# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:57:46 2016

@author: amcurtis91
"""

import mirror


def main():
    #file_1 = open("tetons1.ppm", 'r')
    tiny_file = open("tinypix.ppm", 'r')
    #file_2 = open("tetons2.ppm", 'r')
    #file_3 = open("tetons3.ppm", 'r')
    
    
    in_file = tiny_file
    
    mirror.flip(in_file, "flipped.ppm")
    
main()