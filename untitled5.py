# -*- coding: utf-8 -*-
"""
Anna Ganguly
Gencyber 2016
Caesar Cypher
7/8/16
"""

'''string = "Pokemon GO is addicting"
print(string[8])

seg = string[8:13]

print(seg)'''

"""def caesar_cypher(string,integer):
    empty_string = ''
    for char in string:
        ascii_number = ord(char) + integer
        if ascii_number > 122:
           ascii_number = ascii_number + integer-1
        else:
            empty_string += chr(ascii_number)
    return empty_string             
    
    
print(caesar_cypher('hi,16'))"""

'''def decryptCC(encrypted):
    for i in range (26):
        decrypted = ""
        for char in encrypted:
            asc = ord(char)
            if asc >= 65 and asc <= 91:
                asc -= i
                if asc < 65:
                    asc+= 26
                decrypted += chr(asc)
            elif asc <= 122 and asc >= 97:
                asc -= i
                if asc<97:
                    asc+=26
                decrypted += chr(asc)
            else:
                    decrypted += char
        print(i, decrypted)
    return(i)
            
decryptCC("Zkij te yj")'''
                    
                    
                    
                    
                    
            