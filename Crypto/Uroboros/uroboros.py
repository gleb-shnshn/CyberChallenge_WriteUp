import base64

def encrypt(x, n): 
    key = 'qwertyuioplkjhgfdsazlfmhkb'

    if n == len(x):
        return ''.join(x)

    for i in range(n, len(x)):
        x[i] = chr(ord(x[i]) ^ ord(key[i - n]))    
    
    return encrypt(x, n + 1)

def encrypt_flag(flag):    
    return encrypt(list(flag), 0)    

enc_flag = encrypt_flag(flag)
print repr(enc_flag)

# This script prints "2E\x18fQ)61X@\x10j\x0bjJ+ <\x1fH\x0cuD/Ll" 
