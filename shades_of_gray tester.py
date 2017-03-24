# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:57:58 2016

@author: amcurtis91
"""

import shades_of_gray

def main():
    file_1 = open("tetons1.ppm", 'r')
    #tiny_file = open("tinypix.ppm", 'r')
    #file_2 = open("tetons2.ppm", 'r')
    #file_3 = open("tetons3.ppm", 'r')
    
    
    in_file = file_1
    
    shades_of_gray.neutral(in_file, "shade.ppm")
    
main()