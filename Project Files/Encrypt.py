#!/usr/bin/python
#from Crypto.Cipher import DES3
#from Crypto import Random

#key = b'Sixteen byte key'
#iv = Random.new().read(DES3.block_size)
#cipher = DES3.new(key, DES3.MODE_OFB,'01234567')
#plaintext = b'Hello there I am Sushilk'
#print plaintext

#msg = '01234567' + cipher.encrypt(plaintext)
#print msg

#ptxt = cipher.decrypt(msg)
#print ptxt

from Crypto.Cipher import DES3
from Crypto import Random

iv = Random.get_random_bytes(8)

des31 = DES3.new('0123456701234567', DES3.MODE_CFB,iv)
des32 = DES3.new('0123456701234567', DES3.MODE_CFB,iv)
text = 'kbcdefghabcdefghabcdefghabcdefgh'
cipher_text = des31.encrypt(text)
print cipher_text
plain_text = des32.decrypt(cipher_text)
print plain_text