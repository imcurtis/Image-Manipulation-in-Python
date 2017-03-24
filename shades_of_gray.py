# name: Alex Curtis
# date: 3/23/2016
# file: shades_of_gray.py
# title: shades of gray
# description: replaces each pixels rgb values with the averag of the three
#***************************************

#Steps
#read in files by line
#split them into lists of three
#take the average of each group of three and replace each item
#in the list with the average value

import statistics

def list_handler(in_file):
    l = []
    #for line, to be read through
    #print(type(in_file))
    for line in in_file.readlines():
        #print(type(line))
        #reads through and splits line
        ls = [int(x) for x in line.split()]
        #print(type(ls))
        #adds to line unti completion
        l.extend(ls)
        #print(l)
    return l
  

def neutral(in_file, out_name):
    # gets rid of header, which will be made used again in writing outfile 
    
    magic_number = in_file.readline()
    dimension = in_file.readline().split()
    max_val = in_file.readline()
    #print(type(in_file))
    #print(magic_number)
    #print(dimension)
    #make an empty list of list that will contain the list  of
    # rgb values from each file
    # reads through line, calls list handler function and iterates over
    # multiple files
       
    l = list_handler(in_file)
    # defines length of first list in whole_list, to be used later
    #length = len(whole_list) 
    
    n = 3
    pixels = [l[i:i+n] for i in range(0, len(l), n)]
    #print(pixels)    
    
    
    #defines outfile, outwrites the header    
    outfile = open('shade.ppm', 'w')
    
    outfile.write(magic_number + '\n')
    outfile.write(dimension[0] + ' ' + dimension[1] + '\n')
    outfile.write(max_val + '\n')

    #uses mode function, compares each three files, which we split up
    #by designating length
    for i in pixels:
        int_pixels = [int(x) for x in i]
        avg = int(statistics.mean(int_pixels))
        avg_pixels = [avg]*3
        str_pixels = [str(x) for x in avg_pixels]
        #print(' '.join(str_pixels))
        #writes out mode function
        outfile.write(' '.join(str_pixels) + ' ')
    
    
    outfile.close()
   
#list_handler('tinypix.ppm')
