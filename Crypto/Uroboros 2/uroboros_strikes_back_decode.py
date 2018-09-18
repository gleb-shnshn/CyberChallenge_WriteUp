import base64

flag = str(base64.b64decode("TWEGaEc9C0NIeSYhD08YP1BkIDUFQzJ9"),"utf-8")

def encrypt(x, n): 
    key = 'qwertyuioplkjhgfdsazlfmh'

    if n == len(x):
        return ''.join(x)

    for i in range(n, len(x)):
        x[i] = chr(ord(x[i]) ^ ord(key[i - n]))    
    
    x.insert(0, x.pop((n + 3) % len(x)))

    return encrypt(x, n + 1)

for i in range(3):
    flag=encrypt(list(flag), 0)
    print(flag)

# This script prints "TWEGaEc9C0NIeSYhD08YP1BkIDUFQzJ9" 
