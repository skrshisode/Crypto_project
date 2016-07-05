#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:41:22 2015

@author: HP
"""

from Crypto import Random
from Crypto.PublicKey import RSA

rnf = Random.new().read
RSA_CSyst = RSA.generate(1024, rnf)

f1 = open('SkeyPriv.pem','w')
f1.write(RSA_CSyst.exportKey('PEM'))
f1.close()

f2 = open('SkeyPub.pem','w')
SpubKey = RSA_CSyst.publickey()
f2.write(SpubKey.exportKey('PEM'))
f2.close()

print "Sender's Public Key is published."
