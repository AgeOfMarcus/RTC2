from Crypto.PublicKey import RSA
from Crypto import Random
import hashlib, os

# Private/public keypairs made easy
class key(object):
        def __init__(self):
                random_generator = Random.new().read
                self.priv = RSA.generate(1024, random_generator)
        def encrypt(self,data):
                return self.priv.publickey().encrypt(data,32)[0]
        def decrypt(self, data):
                return self.priv.decrypt(data)
        def export(self, outfile):
                with open(outfile,"wb") as f:
                        f.write(self.priv.exportKey())
        def export_pub(self, outfile):
                with open(outfile,"wb") as f:
                        f.write(self.priv.publickey().exportKey())
        def importkey(self, filename):
                fd = open(filename,"rb")
                keydata = fd.read()
                fd.close()
                return RSA.importKey(keydata)

# Simple sha245 for str and bytes
def sha256(string):
        if list(str(string))[0] == "b":
                try:
                        return hashlib.sha256(string).hexdigest()
                except: pass
        return hashlib.sha256(string.encode()).hexdigest()

# Encode and decode functions (thanks, StackOverflow)
def encode(clear, key):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(enc, key):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
