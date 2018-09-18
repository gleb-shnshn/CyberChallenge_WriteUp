from socket import create_connection

s = create_connection(("prefix.2018.cyberchallenge.ru", 9001))
st="abcdefghijklmnopqrstuvwxyz_0123456789}"
flag1="CC{"
t=s.recv(1024)
while True:
    for i1 in st:
        flag=flag1+i1
        s.send(bytes(flag +'\n',"utf-8"))
        t=s.recv(1024)
        if t!=b'No\n> ':
            print(flag)
            flag1=flag
            break
    if flag1.endswith("}"):
        break
