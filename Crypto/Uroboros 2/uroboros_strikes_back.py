import base64

flag = <flag_was_here>

def encrypt(x, n): 
    key = 'qwertyuioplkjhgfdsazlfmh'

    if n == len(x):
        return ''.join(x)

    for i in range(n, len(x)):
        x[i] = chr(ord(x[i]) ^ ord(key[i - n]))    
    
    x.insert(0, x.pop((n + 3) % len(x)))

    return encrypt(x, n + 1)

enc_flag = base64.b64encode(encrypt(list(flag), 0))
print enc_flag

# This script prints "TWEGaEc9C0NIeSYhD08YP1BkIDUFQzJ9" 
