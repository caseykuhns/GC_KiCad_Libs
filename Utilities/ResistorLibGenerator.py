# Resistor Library builder
# Builds a library of resistors with pricing and PN's from a digikey spreadsheet
# Handy for generating BOM's with useful information for ordering

# TODO
# document how to lay out the example csv here....
# Datasheets, Digi-Key Part Number, Manufacturer Part Number, Manufacturer, Description, Resistance, Tolerance, Power (Watts)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																					



# Using a CSV layout and system time to create new files to prevent overwriting a stable library

import csv
import codecs
from time import gmtime, strftime

FILE_NAME = 'GC_Resistors'
INPUT_FILE = 'test1.csv'

# Line 1 variables
VALUE = 'Resistance'
REF_DES = 'R'
OFFS = ' 0'
PIN_NUM_ON = ' N'
PIN_NAME_ON = ' Y'

# Create the file name string with the added time stamp.
file_name = FILE_NAME + strftime("%H%M%S", gmtime())+'.lib'
# Open the file with write +, "+" creates the file if it doesn't exist
# Using the write option because we don't want to accidentally append 2 libraries in the same file

fOut = open(file_name, "w+")

# We need to add some boiler plate to our file for KiCad

fOut.write("EESchema-LIBRARY Version 2.3\n")
fOut.write("#encoding utf-8\n")

# Open the file we want to read from, this needs to be a .csv with headers

with open(INPUT_FILE, 'rU') as f:
 # Read the file into the 'reader' variable
 reader = csv.DictReader(f)
 for row in reader:
  # For each lib part, we need a header
  fOut.write("#\n")
  fOut.write("# " + row['Resistance'] + "\n")
  fOut.write("#\n")
  print(row['Description'])
  #print(row['Resistance'])      
  #print(row['Datasheets'])
  #print(row['Digi-Key Part Number'])
  fOut.write("DEF " + row['Resistance'] + " " + REF_DES + " 0" + OFFS + PIN_NUM_ON + PIN_NAME_ON + " 1 F N\n")
  fOut.write("F0 \"" + REF_DES + "\" 80 0 40 V V C CNN\n") #Todo, add more parameters here for custom work
  fOut.write("F1 \""  + row[VALUE] + "\" 0 0 30 V V C CNN\n")
  fOut.write("F2 \"\" -70 0 50 V I C CNN\n")
  fOut.write("F3 \"" + row['Datasheets'] + "\" 150 0 40 V I C CNN\n")
  fOut.write("F4 \"" + row['Description'] + "\" 200 0 40 V I C CNN \"Description\"\n")
  fOut.write("F5 \"" + row['Manufacturer Part Number'] + "\" 250 0 40 V I C CNN \"Manufacturer Part Number\"\n")
  fOut.write("F6 \"" + row['Digi-Key Part Number'] + "\" 300 0 40 V I C CNN \"Digi-Key Part Number\"\n")
  fOut.write("F7 \"" + row['Manufacturer'] + "\" 350 0 40 V I C CNN \"Manufacturer\"\n")
  fOut.write("$FPLIST\n")
  fOut.write(" R_*\n")
  fOut.write(" R_*\n")
  fOut.write("$ENDFPLIST\n")
  fOut.write("DRAW\n")
  fOut.write("S -40 -100 40 100 0 1 10 N\n")
  fOut.write("X ~ 1 0 150 50 D 50 50 1 1 P\n")
  fOut.write("X ~ 2 0 -150 50 U 50 50 1 1 P\n")
  fOut.write("ENDDRAW\n")
  fOut.write("ENDDEF\n")
 fOut.write("#")
 fOut.write("#End Library")
 fOut.close()

print("Completed")
