import hashlib

need="2FBBDC6A5FCF7B96B0B1BE4DD33F94A7".lower()

al="abcdefghijklomnopqrstuvwxyz_0123456789"

fla="CC{"

for i1 in al:
    for i2 in al:
        for i3 in al:
            for i4 in al:
                for i5 in al:
                    flag=fla+i1+i2+i3+i4+i5+"}"
                    if hashlib.md5(bytes(flag,"utf-8")).hexdigest()==need:
                        print(flag)
                        
