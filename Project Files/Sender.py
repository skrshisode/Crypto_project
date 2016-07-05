#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:45:34 2015

@author: HP
"""
import sys
#import os
import pickle
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3
from Crypto.Hash import SHA256
#from Crypto.Signature import *
#identification scheme

def fileHandling_module(fpath):
    #fname, ftype = os.path.splitext(fpath)
    try:
        f = open(fpath, "r")
    except IOError:
        print "Error while reading the file: ", fpath
        sys.exit()
    content = f.read()  #read file as binary-bytes & store the content
    f.close()
    return content

def messageEncryption_module(key,ptext):
    iv = Random.get_random_bytes(8)
    TripleDES = DES3.new(key, DES3.MODE_CBC, iv)
    
    if len(ptext) % 16 != 0:
        #ptext += '1'
        #ptext += '0' * (16 - len(ptext) % 16)
        ptext += ' ' * (16 - len(ptext) % 16)
    
    ctext = TripleDES.encrypt(ptext)
    #print ctext
    return iv+ctext
    
def keyEncryption_module(key):
    f = open('RkeyPub.pem','r')
    Rkey_pub = RSA.importKey(f.read())
    f.close()
    enc_key = Rkey_pub.encrypt(key,48)
    return enc_key

def signature_module(mdig):
    f = open('SkeyPriv.pem','r')
    Skey_priv = RSA.importKey(f.read())
    f.close()
    hdig = SHA256.new(mdig).digest()
    sig = Skey_priv.sign(hdig, '')
    return sig

def sender_module(k,d,s):
    f = open('SentData.txt','w')
    f.seek(0)
    f.truncate()
    pickle.dump(k,f)
    pickle.dump(d,f)
    pickle.dump(s,f)
    f.close()
    print "Encrypted data Sent"

#check whether we need additional module

#file_path = input('Enter file-path(e.g. "C:/Documents/file.txt"): ')
file_name = "mymsg.txt"
randomKey = Random.get_random_bytes(16)

msg = fileHandling_module(file_name)
#print msg

encKey = keyEncryption_module(randomKey)
encData = messageEncryption_module(randomKey,msg)
signature = signature_module(msg)

sender_module(encKey,signature,encData)

#print encKey
#print encData
#print signature