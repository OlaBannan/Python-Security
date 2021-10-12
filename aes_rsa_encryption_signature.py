#!/usr/bin/env python
# coding: utf-8

import urllib.request
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

url = 'https://www.cisco.com/index.html'

response = urllib.request.urlopen(url)
data = response.read()

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_EAX)

ciphertext, tag = cipher.encrypt_and_digest(data)
print(ciphertext)

file_out  = open("encrypted.bin", "wb")
[file_out.write(x) for i in (cipher.nonce, tag, ciphertext)]



from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

key = RSA.generate(2048)
private_key = key.export_key()
with open("private.pem", "wb") as file_out:
    file_out.write(private_key)
    
public_key = key.publickey().export_key()
with open("public.pem", "wb") as file_out:
    file_out.write(public_key)
    
data = ("Hello ItWorks!" * 10).encode("UTF-8")

file_out = open("encrypted_data.bin", "wb")

receipent_key = RSA.import_key(open("receiver.pem").read())
session_key = get_random_bytes(16)

cipher_rsa = PKCS1_OAEP.new(receipent_key)
enc_session_key = cipher_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

print(ciphertext, enc_session_key, cipher_aes.nonce, tag)



from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

message = b'I want to sign on this message with my private key!'
message = message * 100000
key = RSA.import_key(open('private.pem').read())
h = SHA256.new(message)
signature = pkcs1_15.new(key).sign(h)

print(signature)

key = RSA.import_key(open('public.pem').read())
h = SHA256.new(message)

pkcs1_15.new(key).verify(h, signature)
print("Valid!")
    





