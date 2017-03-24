# name: Alex Curtis
# date: 3/11/2016
# file: effects.py
# title: object filter
# description: this function takes multiple images, and produces the most 
# common pixel value at each position
#***************************************

import statistics

def list_handler(in_file_list):
    l = []
    #for line, to be read through
    for line in in_file_list.readlines():
        print(type(line))
        #reads through and splits line
        ls = line.split()
        #adds to line unti completion
        l.extend(ls)
    return l
  

def object_filter(in_file_list, out_name):
    # gets rid of header, which will be made used again in writing outfile
    for f in in_file_list:    
    
        magic_number = f.readline()
        dimension = f.readline().split()
        max_val = f.readline()
    
    #make an empty list of list that will contain the list  of
    # rgb values from each file
    whole_list = []
    # reads through line, calls list handler function and iterates over
    # multiple files
    for f in in_file_list:    
        whole_list.append(list_handler(f))
    # defines length of first list in whole_list, to be used later
    length = len(whole_list[0])
    
    #defines outfile, outwrites the header    
    outfile = open('out.ppm', 'w')
    
    outfile.write(magic_number + '\n')
    outfile.write(dimension[0] + ' ' + dimension[1] + '\n')
    outfile.write(max_val + '\n')

    #uses mode function, compares each three files, which we split up
    #by designating length
    for i in range(length):
        mode = statistics.mode([whole_list[0][i], whole_list[1][i], whole_list[2][i]])
        #writes out mode function
        outfile.write(mode + ' ')
    
    

    
    
    
    outfile.close()
   
    
#list_handler(in_file_list)
