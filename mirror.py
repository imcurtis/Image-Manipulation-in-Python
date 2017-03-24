# name: Alex Curtis
# date: 3/24/2016
# file: mirror.py
# title: mirror
# description: flips the image on its side, tiger style
#***************************************

def list_handler(in_file):
    l = []
    #for line, to be read through
    #print(type(in_file))
    for line in in_file.readlines():
        #print(type(line))
        #reads through and splits line
        #reversedLine = line[::-1]
        ls = [int(x) for x in line.split()]
        #print(type(ls))
        #adds to line unti completion
        l.extend(ls)
        #print(l)
    return l
  

def flip(in_file, out_name):
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
    
    #for line in l:        
    #new_l = l[::-1]
        # defines length of first list in whole_list, to be used later
        #length = len(whole_list) 
    
    n = 3
    pixels = [l[i:i+n] for i in range(0, len(l), n)]
    #reversedPixels = [l[::-1] for i in range(0, len(pixels), n)] 
    #print(pixels)
    
    chunks=[pixels[x:x+len(dimension[0])] for x in range(0, len(pixels), len(dimension[0]))]
    
    for i in chunks:   
        reverse_c = i[::-1]
        print(reverse_c)
    
    #defines outfile, outwrites the header    
    outfile = open('flipped.ppm', 'w')
    
    outfile.write(magic_number + '\n')
    outfile.write(dimension[0] + ' ' + dimension[1] + '\n')
    outfile.write(max_val + '\n')

    #uses mode function, compares each three files, which we split up
    #by designating length

    for i in reverse_c:
        #int_pixels = [int(x) for i in reverse_c for x in i]
        #print(int_pixels)
        #avg = int(statistics.mean(int_pixels))
        #avg_pixels = [avg]*3
        str_pixels = [str(x) for x in i for i in reverse_c]
        #print(str_pixels)
        #flipped_pixels = str_pixels[::-1]
        #print(' '.join(str_pixels))
        #writes out mode function
        outfile.write(' '.join(str_pixels) + ' ')
    
    
    outfile.close()


