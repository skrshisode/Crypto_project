#!/usr/bin/python

message = "Hi there! This is msg strng."
print "original: ",message
print '---begin---'

#from Crypto import Random

#from Crypto.Hash import SHA256

#hash = SHA256.new()
#hash.update(message)
#print hash.digest()

from Crypto.Cipher import DES3

key = b'Sixteen byte key'
iv = Random.new().read(DES3.block_size)
#iv = key
cipher = DES.new(key, DES1.MODE_OFB, iv)
plaintext = message
ciphertxt = cipher.encrypt(plaintext)
print "cipher: ",ciphertxt
msg = iv + ciphertxt
print "op: ",msg
print '---end---'