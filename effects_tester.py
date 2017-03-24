# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:15:07 2016

@author: amcurtis91
"""

import effects

def main():
    file_1 = open("tetons1.ppm", 'r')
    file_2 = open("tetons2.ppm", 'r')
    file_3 = open("tetons3.ppm", 'r')
    
    
    in_file_list = [file_1, file_2, file_3]
    
    effects.object_filter(in_file_list, 'out.ppm')
    
main()