#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Performs tests using the validation API.
    Author: Muhammad Umair
    Created: Apr 07, 2016
    Usage examples: python Tests.py codes code_file_name
                    python Tests.py formats formats_file_name.txt
    Python version: 2.7.5
'''

from ValidateUKCodes import validate, format_code
import sys

def codes(filename):
    try:
        with open(filename, 'r') as codes_file :
            codes = codes_file.read()
            codes = codes.split('\n')
            for code in codes:
                if len(code) > 0:
                    validate(code)
    except IOError:
        print 'File not found. %s' %filename
        raise SystemExit
    except:
        print 'File %s format not valid.' %(filename)
        raise SystemExit

def formats(filename):
    try:
        with open(filename, 'r') as formats_file:
            formats = formats_file.read()
            formats = formats.split('\n')
            for formatt in formats:
                if len(formatt):
                    (area, district, sector, unit) = formatt.split(' ')
                    format_code(area, district, sector, unit)
    except IOError:
        print 'File not found. %s' %filename
        raise SystemExit
    except:
        print 'File %s format not valid.' %(filename)
        raise SystemExit

def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: python Tests.py codes/formats filename')
    if len(sys.argv) == 3:
        if sys.argv[1] == 'codes':
            codes(sys.argv[2])
        elif sys.argv[1] == 'formats':
            formats(sys.argv[2])
    else:
        print 'Invalid arguments.'

if __name__ == '__main__':
    main()
