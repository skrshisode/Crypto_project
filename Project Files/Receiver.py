#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:31:50 2015

@author: HP
"""
#import sys
#import os
import pickle
#from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3
from Crypto.Hash import SHA256
#from Crypto.Signature import *
#identification scheme

def receiver_module():
    f = open('SentData.txt','r')
    k = pickle.load(f)
    d = pickle.load(f)
    s = pickle.load(f)
    f.close()
    return k,d,s

def Verification_module(mdig,sig):
    f = open('SkeyPub.pem','r')
    Skey_pub = RSA.importKey(f.read())
    f.close()
    hdig = SHA256.new(mdig).digest()
    
    if Skey_pub.verify(hdig, sig):
        print "Identity verified"
    else:
        print "Couldn't verify indentity of sender"

def keyDecryption_module(eKey):
    f = open('RkeyPriv.pem','r')
    Rkey_priv = RSA.importKey(f.read())
    f.close()
    key = Rkey_priv.decrypt(eKey)
    return key

def messageDecryption_module(key,eData):
    iv = eData[0:8]
    TripleDES = DES3.new(key, DES3.MODE_CBC, iv)
    ctext = eData[8:len(eData)]
    ptext = TripleDES.decrypt(ctext)
    #print ptext
    ptext = ptext.rstrip()
    return ptext

#def identification_module():
    #Add your code

def fileHandling_module(text): 
    f = open('Receivedfile.txt','w')
    f.seek(0)
    f.truncate()
    f.write(text)
    f.close()
    print "File received successfully."

encKey,signature,encData = receiver_module()

Key =  keyDecryption_module(encKey)
Ptext = messageDecryption_module(Key,encData)

Verification_module(Ptext,signature)
fileHandling_module(Ptext)
