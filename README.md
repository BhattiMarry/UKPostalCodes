# UKPostalCodes

A python API which facilitates the validation and formatting of UK postal codes.

Main API file: ValidateUKCodes.py

API has two functions;

1. Validate: It takes the UK postal code as a string and tries to validate it.

2. Format: It takes 4 arguements, Area, Distric, Sector and Unit respectively. It returns the finalized, formatted postal code according to the parameters given.

Test Script: Tests.py

This script runs two files, one having some codes to validate and the other file having some code-fragments (Area, Sector etc) to make/format the codes. While validating this API, try to run this script having your own data in the test-data files.

There are two ways to running this test script;

1. python Tests.py formats format_file_name 
2. python Tests.py codes codes_file_name

The first is to run the formats file upon API. This will try to read the formats file, on each line it will try to make a postal code which then is validated.

The second method will try to validate the codes in codes_file found line by line in file.

Test data files: codes, formats.txt

The files has a number of test cases for the API, one on each line.

Usage:

Download the API script file, and place it in either;

1. The main directory in which you want to use it.

2. The python library directory "/lib/python2.7/site-packages". While doing this, you can import it like any other python API or library.

Note: This API and its test script works fine on python version 2.7.5. 
