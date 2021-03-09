BUSINESS CASE PART


TASK 1

1. Load and merge all files Table_* using pandas package
2. Drop duplicates if any appear in data
3. Show (for example print) number of null values in each column
4. Fill numerical null values with 1337
5. For each row calculate difference (number of days) between Acctg Date and Date columns
6. For each row calculate difference (number of BUSINESS days) between Acctg Date and Date columns (ignore weekends and UK bank holidays)
7. Convert Amount to PLN using FXrates.csv
8. Create folder results and save separate file for EACH unique Type value, use Type in name of saved file (for example Table_4P4.xlsx)


GENERAL PROGRAMMING PART


TASK 1

Write Morse code decoder. https://en.wikipedia.org/wiki/Morse_code
decoder('.- -   -.. .- .-- -.   .-.. --- --- -.-   - ---   - .... .   . .- ... -')
Should return "AT DAWN LOOK TO THE EAST". Letters are separated by one whitespace, words by three whitespaces.

TASK 2

Write a programm which encodes a sentence: for each word which length exceeds 3 letters return that word in backward order. 
For example:

AT DAWN LOOK TO THE EAST  - input

AT NWAD KOOL TO THE TSAE  - result
