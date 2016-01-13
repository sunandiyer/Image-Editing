# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:41:59 2015

@author: Sunand Iyer
UNI: sri2117

Has a main function that asks user for what file they want to edit and which
effect they would like to use. Applies that effect to the image.
"""

import effects

def main():

    effectsList = [False] * 6    
    
    inFile = input("What is the file you want to read in (.ppm): ")

    outFile = input("What is the name of the file you want to output (.ppm): ")
    
    filterUse = input("Here is a list of filters:" + "\n" + 
    "0 is object_filter \n" +
    "1 is shades_of_gray \n" + 
    "2 is negate_red \n" +
    "3 is negate_green \n" +
    "4 is negate_blue \n" +
    "5 is mirror \n" + 
    "Which filter would you like (only choose 1 filter): ")  
    
    effectsList[int(filterUse)] = True
    
    extraFileList = []  
    ask = True
    
    if effectsList[0] == True:
        while ask == True:
            wantExtraFile = input("Any other files you want to add (y/n): ")
            if wantExtraFile == 'y':
                extraFile = input("What is the name of the file you want to " + 
                "add (.ppm): ")
                extraFileList.append(extraFile)
            else:
                ask = False
        
    effects.apply_effects(inFile, outFile, effectsList, *extraFileList)
  
  
main()