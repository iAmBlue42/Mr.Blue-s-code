# telegraph.py
# Nathaniel Johnson

# How to use: This script is run in the command line. To run type the path to this script followed by two arguments; the first argument is the file to be converted, the cipher text. The second argument is the output file. If the output file already exists you will be asked if you want to overwrite. If you say know you will be asked to choose a different filename. If you do not specify a path the output file will be wherever you are in the command line. The examples are meant to be normie friendly, if you are a Linux Chad, or know at all what you are doing these instructions are not for you. 

# Example, relative path: telegraphy.py cipher.txt converted.txt
# Example, absolute path: C:\Users\user\Desktop\telegraph.py C:\Users\user\Documents\cipher.txt C:\Users\user\Desktop\converted.txt

# Purpose: This script converts any text file to a format that is easier to perform manual cryptography analysis; 10 collums of 5 Uppercase characters.
# bugs: error when special characters that windows doesn't like are used for output filea. debateable whether this is worth fixing or adding error handling.

import sys

# Explanation: The Main function takes the 2nd and 3rd arguments, the input file and output file. By default the output_file is set to the 3rd argument (sys.argv[2]), but if the user decides to not overwrite and changes the output file in the create_out function, the new output_file is returned to the main function. This function passes the 2nd argument to the strip_whitespace function and then that function returns a string that is stored in the stripped variable. The the create_out function is called which Main passes the stripped and output_file variables to.  
def main(output_file = sys.argv[2]):
    print("Input file =", sys.argv[1], "\nOutput file =", output_file)
    stripped = strip_whitespace(sys.argv[1])
    create_out(stripped, output_file)

def create_out(input_file, output_file):
    
    try:
        create = open(output_file,'x')
        create.close
        convert(input_file, output_file)
    except:
        overwrite = str(input("Output file already exists overwrite?(Y/N) "))
        if overwrite == 'y':
            convert(input_file, output_file, 'w')
        else:
            output = input("Choose a different file name: ")
            main(output)

# Explanation: strip whitespace. reads txt and put everything on one line. Then stores this list in a variable "lines". Lines is then stored as a string, and then the [' and '] are removed, and returns the text from the file as a string of characters with no spaces on one line to main
# Note for improvement: This is very messy and could probably be condensed on fewer lines. broke when breifly attempted.
def strip_whitespace(input_file):
    try:

        with open(input_file, 'r') as crypt:
            lines = crypt.readlines()
            lines = [line.replace(' ', '') for line in lines]
            #Uncomment the lines bellow to remove different puntuation, not sure why you'd want to, but hey I spent 5 seconds adding it and its an option.
            #lines = [line.replace(',', '') for line in lines]
            #lines = [line.replace('.', '') for line in lines]
            #lines = [line.replace('?', '') for line in lines]
            #lines = [line.replace('!', '') for line in lines]


            lines = str(lines)
            lines = lines[2:-2]
            crypt.close
            return lines
    except:
        print("Input file not found.\nTry again.")
        quit()

        

# Explanation: Convert. Takes the string output by "strip_whitespace" and formats it for cryptographic analysis. Adds a space after every 5 characters and a newline charater after every 60 characters. Then the formated string is saved to the designated output file.
def convert(input_file, output_file, a_or_w = 'a'):

    # Change the two fives to a different number on the first line bellow if you want there to be a space after a different number of characters.
    # Change the two 60s to a different number on the second line bellow if you want to the to be more collums per line in the output, to make collums even this involves some basic math. for example if you wanted 20 collums instead of 10 you would change both to 120.
    conv_line = ' '.join(input_file[i:i + 5] for i in range(0, len(input_file), 5))
    conv_line = '\n'.join(conv_line[i:i + 60] for i in range(0, len(conv_line), 60))

    # Comment out the line bellow if you do not want the converted text printed on the command line.
    print(conv_line.upper())
     
    with open(output_file, a_or_w) as spaced:
        spaced.write(conv_line.upper())
    spaced.close

main()
