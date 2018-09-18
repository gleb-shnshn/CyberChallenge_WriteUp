import requests
from socket import create_connection
import json

def game():
    s = create_connection(("tictactoe.2018.cyberchallenge.ru", 9002))
    player="X"
    a=0
    t=s.recv(1024)
    print(str(t,"utf-8"))
    k=0
    s.send(bytes("0 0"+"\n","utf-8"))
    state="X--------"
    while a==0:
        t=s.recv(1024)
        if k>98:
            print(str(t,"utf-8"))
        if "x y" not in str(t,"utf-8") or "go" in str(t,"utf-8") :
            print(str(t,"utf-8"))
            if "loosers" in str(t,"utf-8"):
                a=1
                break
            t=str(t,"utf-8")
            if "." in t:
                t=t[t.index(".")+1:]
                t=bytes(t,"utf-8")
            else:
                print(t)
            k+=1
            print(k)
        state = str(t,"utf-8").replace("\n","").replace("-","").replace(">","").replace("x y","").replace(" ","").replace("0","").replace("1","").replace("2","").replace("o","O").replace("x","X").replace("_","-")

        response = requests.get("https://stujo-tic-tac-toe-stujo-v1.p.mashape.com/"+state+"/"+player,
          headers={
            "X-Mashape-Key": "place for your api key",
            "Accept": "application/json"
          }
        )
        resp_rec=json.loads(response.text)["recommendation"]
        x=resp_rec//3
        y=resp_rec%3
        s.send(bytes(str(x)+" "+str(y)+"\n","utf-8"))
    return 0
while game()==0: pass
