#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:25:02 2015

@author: HP
"""

from Crypto import Random
from Crypto.PublicKey import RSA

rnf = Random.new().read
RSA_CSyst = RSA.generate(1024, rnf)

f1 = open('RkeyPriv.pem','w')
f1.write(RSA_CSyst.exportKey('PEM'))
f1.close()

f2 = open('RkeyPub.pem','w')
RpubKey = RSA_CSyst.publickey()
f2.write(RpubKey.exportKey('PEM'))
f2.close()

print "Receiver's Public Key is published."
