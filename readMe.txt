Name: Sunand Iyer
UNI: sri2117

Disclaimer: 
All functions assume that reading in one line is equal to one row of the image.

File Name: effects.py

Function Name: get_nRows(inFile, outfile)

Function takes in two file objects. It writes out the first line of the input file 
object to the output file object. It then stores the second line of the input file. 
If then splits the second lines and gets the number of rows. The function also writes
out the second line to the output file. The function then returns the number of rows,
output file, and the input file.

Function Name: getMaxVal(inFile, outfile)

Function takes in two file objects. It reads in the third line of the input file and
stores it in a variable called thirdLine. It then writes out the third line to the output 
file. The function then splits the thirdLine and and gets the maximum value that each RGB 
value can be. It then returns the maximum value, the input file object, and the output file
object.

Function Name: openBoth(infile, outfile)

The functions takes in two file names in string format. The function then opens both of
these files and returns the file objects.

Function Name: apply_effects(in_filename, out_filename, effects, *filter_filenames)

Function takes in 2 file names (string format), with one being an input file and the
other being the output file. It also takes in a list of Booleans to determine which effect
to use. The last input is additional files that the function will take and store as a tuple.
The function then looks at the list of Booleans. In this list, only one value will be True. 
The list has length 6. The function uses if and elif statements to check which index is 
equal to True. Once it identifies which index is True, it then calls the openBoth function
to open the files. It then calls whichever function is associated with effect that is 
associated with the index.

Function Name: object_filter(in_file_list, out_file)

The function takes in a list of file objects and a file object for the output file. The function
first looks at the first file object. Since it is assumed that each file has the same number of rows,
the get_nRows is called on the first file object to get the number of rows in the file. I then wrote 
out the third line of the file to the output file because the third line is always 255. I then wrote a for 
loop which just iterated through the first three lines to get the other file objects to the same position
as the first file object. I then iterated through each file object and appended each line to a list and then
appended that list (which contained all the lines for a file) to a larger list which stored all the lines from
all of the files. I then close each file object. I then calculated the total number of lines in each of the file 
objects (assumed to be the same for all files). I then iterated through each line and then each element in each line
for each file to store the individual RGB value from each file. I then used Counter (imported from collections) to 
find which pixel value was the most common. The function then writes out this value to the output file. After each 
line, I create a new line. The function then closes the file.

Function Name: shades_of_gray(in_file, out_file)

The function takes in two file objects, one as the input file and one as the output file. The function calls the
get_nRows function to get the number of rows. The function then iterate through the total number of rows and then 
through each element of the row. The function finds the average RGB value of each pixel and sets all RGB values in 
the pixel to this average value. The function then writes out the pixels row by row. The file object is then closed.

Function Name: negate_red(in_file, out_file)

The function takes in two file objects, one as the input file and one as the output file. The function calls the 
get_nRows functions to get the number of rows. The function then calls in the getMaxVal function to get the 
maximum value that each RGB value can be. The function then iterates through each row and each element of each row.
If the index was in the red position, the function just replaces that value with the maximum value - current value.
The green and blue values remain the same. The function then writes out the pixels row by row. The file object is 
then closed.

Function Name: negate_green(in_file, out_file)

The function takes in two file objects, one as the input file and one as the output file. The function calls the 
get_nRows functions to get the number of rows. The function then calls in the getMaxVal function to get the 
maximum value that each RGB value can be. The function then iterates through each row and each element of each row.
If the index was in the green position, the function just replaces that value with the maximum value - current value.
The red and blue values remain the same. The function then writes out the pixels row by row. The file object is 
then closed.

Function Name: negate_blue(in_file, out_file)

The function takes in two file objects, one as the input file and one as the output file. The function calls the 
get_nRows functions to get the number of rows. The function then calls in the getMaxVal function to get the 
maximum value that each RGB value can be. The function then iterates through each row and each element of each row.
If the index was in the blue position, the function just replaces that value with the maximum value - current value.
The green and red values remain the same. The function then writes out the pixels row by row. The file object is 
then closed.

Function Name: mirror(in_file, out_file)

The function takes in two file objects, one as the input file and one as the output file. The function calls the 
get_nRows functions to get the number of rows. The function then writes out the third line of the input file.
The function then iterates through all the rows and each element in the row. I set a variable called counter to be
equal to the length of each line - 1. I create a while loop for when counter is greater than or equal to 0, that captures
the values by pixel (hence the if statement where (counter + 1) % 3 == 0). Since the counter starts from the end index, I just
index the line by counter to write out the pixels in reversed order. I decrease counter by 1 through each iteration. The function
then writes out each row. The file is then closed.

File Name: effects_tester.py

Function Name: main()

I initialize a list called effectsList to be all False. Since the program applies one effect at a time, the list will only have one
True value at a time. I ask the user for the name of an input file and the name of an output file. I then ask the user which
effect they want. Based on the integer they input (a certain integer corresponds with a certain effect), the function changes
that index in effectsList to be true. The function then has an if statement for the situation where the user wants to call the
objects_filter function because this function takes more than 1 file as an input. The function uses a while loop with a variable
called ask being set to True. The user is asked if they want to input extra file and if they do, they are then asked to name the input 
file. If they do not want to input an extra file, then ask is set to False and the loop is exited. The apply_effects function is then called.



                                    