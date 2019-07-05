import requests
import json

def Sor(question):
	USERNAME = '<Username Here>'
	TOKEN = '<token here>'
	message = {'username':USERNAME, 'token':TOKEN,'code':question,'type':'text'}
    r=requests.post("https://beta.ceyd-a.com/jsonengine.jsp",data=message)
    print(json.loads(r.text[1:-3]).get('answer'))

while True:
    soru = input("Ne sormamı istersin(Çıkmak için 'çıkış'):")
    if soru=="çıkış":
        break
    Sor(soru)
