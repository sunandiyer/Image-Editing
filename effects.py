"""
effects module for assignment 4
Date: 11/8/15

@author: Sunand Iyer
UNI: sri2117

File contains functions that can be used to edit an image. 

"""

#import statistics
from collections import Counter


def get_nRows(inFile, outfile):
    '''Gets the number of rows with pixels in the input file'''
    
    outfile.write(inFile.readline())
    
    secondLine = inFile.readline()
    outfile.write(secondLine)
    nRows = int(secondLine.split()[1])
    
    return (nRows, outfile, inFile)


def getMaxVal(inFile, outfile):
    '''Gets the maximum value that each RGB value can be'''
    
    thirdLine = inFile.readline()
    outfile.write(thirdLine)
    maxVal = thirdLine.split()[0]
    return(maxVal, inFile, outfile)
    

def openBoth(infile, outfile):
    '''Function open the infile and the outfile'''
    
    inFile = open(infile, "r")
    outFile = open(outfile, "w")
    return(inFile, outFile)


def apply_effects(in_filename, out_filename, effects, *filter_filenames):
    '''primary function that is called by the effects_tester. 
    in_filename the name the primary input file 
    out_filename refers is the name of the output file
    effects is a list of booleans where each position indicates whether we want
    that effect activated
	effects[0] object_filter
 	effects[1] shades_of_gray
	effects[2] indicates negate_red
	effects[3] indicates negate_green
	effects[4] indicates negate_blue
	effects[5] indicates mirror

	*filter_filenames stores the names of additional files for the object_filter


	'''
     
    if effects[0] == True:
        inFileList = [open(in_filename, "r")] 
        for file in filter_filenames:
            inFileList.append(open(file, "r"))
        outFile = open(out_filename, "w")  
        object_filter(inFileList, outFile)
    
    elif effects[1] == True:
        inFile, outFile = openBoth(in_filename, out_filename)        
        shades_of_gray(inFile, outFile)
    
    elif effects[2] == True:
        inFile, outFile = openBoth(in_filename, out_filename)         
        negate_red(inFile, outFile)
        
    elif effects[3] == True:
        inFile, outFile = openBoth(in_filename, out_filename) 
        negate_green(inFile, outFile)
        
    elif effects[4] == True:
        inFile, outFile = openBoth(in_filename, out_filename) 
        negate_blue(inFile, outFile)
        
    elif effects[5] == True:
        inFile, outFile = openBoth(in_filename, out_filename) 
        mirror(inFile, outFile)
        

def object_filter(in_file_list, out_file):
    '''Filters out pixel values that appear in only a minority
    of the images in the parameter in_file_list'''
    
    file1 = in_file_list[0]
    nRows, outFile, inFile1 = get_nRows(file1, out_file)
    outFile.write(inFile1.readline()) 
    totLines = []
    
    for file in in_file_list[1:]:
        for i in range(3):
            file.readline()
    for file in in_file_list:
        linesList = []
        for i in range(nRows):
            linesList.append(file.readline().split())
        totLines.append(linesList)
        file.close()
    
    file1Lines = totLines[0]
    for k in range(len(file1Lines)):
        outputPixelList = []
        for i in range(len(file1Lines[k])):
            pixelList = []
            for fileList in totLines:
                pixelValue = fileList[k][i]
                pixelList.append(pixelValue)
            finPixVal = Counter(pixelList).most_common(1)[0][0]
            outputPixelList.append(finPixVal)
        
        outFile.write('  '.join(outputPixelList)+'\n')
    outFile.close()


def shades_of_gray(in_file, out_file):
    '''Converts the color image in_file to black and white'''
    
    nRows, outfile, inFile = get_nRows(in_file, out_file)
    outfile.write(inFile.readline())
    
    for i in range(nRows):
        
        line1 = inFile.readline().split()
        pixelList = []
        for i in range(len(line1)):
            if (i+1) % 3 == 0:
                avgVal = str(int(sum([int(line1[i - 2]), int(line1[i - 1]), \
                int(line1[i])]) / 3))
                pixelList.append(avgVal)
                pixelList.append(avgVal)
                pixelList.append(avgVal)
        outfile.write('   '.join(pixelList)+ '\n')
    outfile.close()


def negate_red(in_file, out_file):
    '''Negates the red in an image'''
        
    nRows, outfile, inFile = get_nRows(in_file, out_file)   
    maxVal, inFile, outfile = getMaxVal(inFile, outfile)
    
    for i in range(nRows):
        line1 = inFile.readline().split()
        pixelList = [] 
        for i in range(len(line1)):
            if i % 3 == 0 and i + 2 <= len(line1):
                pixelList.append(str(int(maxVal) - int(line1[i])))
                pixelList.append(line1[i+1])
                pixelList.append(line1[i+2])
        outfile.write('   '.join(pixelList)+ '\n')
    outfile.close()
    
            
def negate_green(in_file, out_file):
    '''Negates the green in an image'''
    
    nRows, outfile, inFile = get_nRows(in_file, out_file) 
    maxVal, inFile, outfile = getMaxVal(inFile, outfile)
    
    for i in range(nRows):
        line1 = inFile.readline().split()
        pixelList = []
        for i in range(len(line1)):
            if (i - 1) % 3 == 0:
                pixelList.append(line1[i-1])
                pixelList.append(str(int(maxVal) - int(line1[i])))
                pixelList.append(line1[i+1])
        outfile.write('   '.join(pixelList)+ '\n')
    outfile.close()
 
   
def negate_blue(in_file, out_file):
    '''Negates the blue in an image'''    
    
    nRows, outfile, inFile = get_nRows(in_file, out_file)   
    maxVal, inFile, outfile = getMaxVal(inFile, outfile)
    
    for i in range(nRows):
        line1 = inFile.readline().split()
        pixelList = []
        for j in range(len(line1)):
            if (j + 1) % 3 == 0:
                pixelList.append(line1[j-2])
                pixelList.append(line1[j-1])
                pixelList.append(str(int(maxVal) - int(line1[j])))
        outfile.write('   '.join(pixelList)+ '\n')
    outfile.close()


def mirror(in_file, out_file):
    '''Creates a mirror image by flipping an image horizontally''' 
    
    nRows, outfile, inFile = get_nRows(in_file, out_file)   
    thirdLine = inFile.readline()
    outfile.write(thirdLine)
    
    for i in range(nRows):
        line1 = inFile.readline().split()
        pixelList = [] 
        counter = len(line1) - 1
        while counter >= 0:
            if (counter + 1) % 3 == 0:
                pixel = [line1[counter - 2], line1[counter - 1], line1[counter]]
                pixelList.extend(pixel)
            counter = counter - 1
        outfile.write('   '.join(pixelList) + '\n')
    outfile.close()     
    
                
                
    


   
            
    
        
        
        
    
    