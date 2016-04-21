#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''An api to validate and format of UK postcodes.
   Formatting and validation rules got from: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
   Author: Muhammad Umair Bhatti
   Creted: Apr 07, 2016
   Version: 1.0
   uses Python version: 2.7.5
'''

third = 'ABCDEFGHJKPSTUW'
forth = 'ABEHMNPRVWXY'
'''
    Validate module to that validates the post code according to postcode parts.
    Params: UK postcode
    Functionality: Validates the postcode and prompts the user if its valid or not
    return: True/False
'''
def validate(code):
    code1 = str(code)
    if len(code1) not in [6, 7, 8]:
        print 'Code length is not valid'
        return
    if ' ' not in code1:
        print 'Not a valid code. No space'
        return
    (inward, outward) = code1.split(' ')

    if validate_inward(inward):
        if validate_outward(outward):
            print '%s: Valid' %code

'''
    Validation of inward part of code module.
    Params: inward part of code
    Functionality: validates the postcode Area and postcode District
    return: True/False
'''
def validate_inward(inward):
    for character in inward:
        char = ord(character)
        if char not in range(48, 58) and char not in range(65, 93):
            print 'non character found: %s' %(chr(char))
            return False
    length_inward = len(inward)
    if length_inward in [2, 3, 4]:
        if ord(inward[0]) in range(65, 93):
            if inward[0] in ['Q', 'V', 'X']:
                print 'Q V X found at 1st position in INWARD'
                return False
            if ord(inward[1]) in range(65, 93):#2nd char is Char, 3-4
                if ord(inward[1]) in [73, 73, 90]:
                    print 'I, J, Z found at 2nd position in INWARD'
                    return False
                if length_inward is 3:
                    if ord(inward[2]) in range(48, 58):
                        pass
                    else:
            		    print '3rd char must be a digit in this type of structure.'
            		    return False
                if length_inward is 4:
                    char = ord(inward[3])
                    if char in range(48, 58):
                        pass
                    elif char in range(65, 93):
                        if chr(char) not in list(forth):
                		    print 'non character %s from the list found at 4th from the list: %s' %(chr(char), forth)
                		    return False	                        
                    else:
            		    print 'non character found: %s' %inward[3]
            		    return False
            elif ord(inward[1]) in range(48, 58):#2nd char is Number, 2-3
                if length_inward is 2:
                    pass
                elif length_inward is 3:
                    char = ord(inward[2])
                    if char in range(48, 58):
                        pass
                    elif char in range(65, 93):
                        if chr(char) not in list(third):
    		                print 'non character found at 3rd from the list: %s' %(third)
        	                return False
                    else:
                        print 'non character found: %s' %(chr(char))
                        return False
                else:
    		        print 'length not correct, should be 2, 3'
    		        return False

            else:
                print 'non character found: %s' %(inward[1])
                return False
        else:
            print 'First character is not an alphabet.'
            return False
    else:
        print 'bad length, should be 2-4'
        return False
    return True

'''
    Validation of outward part of code module.
    Params: outward part of code
    Functionality: validates the postcode sector and postcode unit
    return: True/False
'''

def validate_outward(outward):
    for character in outward:
        char = ord(character)
        if char not in range(48, 58) and char not in range(65, 93):
            print 'non character found: %s' %character
            return False
    length_outward = len(outward)
    if length_outward is 3:
        if ord(outward[0]) not in range(48, 58):
            print 'Not a digit as first character in OUTWARD.'
            return
        for i in range(1, length_outward):
            char = ord(outward[i])
            if char in range(65, 93):
                pass
            else:
                print 'Must be alphabet, the last 2 character in OUTWARD'
                return
    else:
        print 'Bad length of OUTWARD. Must be 3'
        return
    return True

'''
    Formatting module of postcode according to given postcode Area, District, Sector and Unit respectively.
    Params: postcode Area, postcode District, postcode Sector, postcode Unit, 
    Functionality: Formats the postcode according to given parameters.
    return: True/False according to built postcode
'''

def format_code(area, district, sector, unit):
    code = ''
    code += str(area)
    code += str(district)
    code += ' '
    code += str(sector)
    code += str(unit)
    validate(code)
