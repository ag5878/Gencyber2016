# -*- coding: utf-8 -*-
"""
Anna Ganguly
Gencyber
More ciphers
7/19/16
"""
'''def RSA_cipher(message, prime1, prime2, publickey):
    n = prime1 * prime2
    encryption = (message **publickey) %n
    print(encryption)
    
RSA_cipher(65,31,29,13)'''

"""import qrcode
img = qrcode.make('red velvet cheescake is the best kind of cheesecake')
img.show()
img.save('filename.png')"""
    
import base64
encoded = base64.b64encode(b'apple pie')
print(encoded)