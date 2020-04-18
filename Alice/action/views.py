from django.shortcuts import render
from .endecrypt import *
# Create your views here.
from django.http import HttpResponse,JsonResponse
import requests
import json
import socket
import time
Ka=34567
def gettgt(request):
    client_id = "Alice"
    service_id = "AS"
    keyword = {"client_id":client_id,"service_id":service_id}

    r=requests.post('http://127.0.0.1:8001/service/givetgt/',keyword)

    data = r.json()
    #print(json.loads(r.text))
    #print(r)
    en_Ka_tgs=data['en_Ka_tgs']
    en_TGT=data['en_TGT']

    Ka_tgs=int(decrypt(Ka,en_Ka_tgs))
    TGT=decrypt(Ka,en_TGT)
    Ka_tgsFile = open("./Ka_tgs.txt","w+")
    Ka_tgsFile.write(str(Ka_tgs))
    TGTFile = open("./TGT.txt","w+")
    TGTFile.write(TGT)
    return JsonResponse(data)


def getsgt(request):
    client_id = "Alice"
    server_id = "Bob"

    time_stamp = time.time()
    lifetime = 600
    Ka_tgsFile = open("./Ka_tgs.txt", "r+")
    Ka_tgs = Ka_tgsFile.read()
    Ka_tgs = int(Ka_tgs)
    TGTFile = open("./TGT.txt", "r+")
    TGT = TGTFile.read()

    Auth = {
        "client_id": client_id,
        "server_id": server_id,
        "client_address":"127.0.0.1",
        "time_stamp":time_stamp,
        "lifetime":lifetime
    }

    en_Auth = encrypt(Ka_tgs,str(Auth))
    keyword={
        "en_Auth":en_Auth,
        "TGT":TGT
    }
    print(keyword)
    r = requests.post('http://127.0.0.1:8001/service/givesgt/', keyword)
    data = r.json()

    en_Ka_b = data['en_Ka_b']
    en_SGT = data['en_SGT']

    Ka_b = int(decrypt(Ka_tgs,en_Ka_b))
    SGT = decrypt(Ka_tgs, en_SGT)
    print("Ka_b: ")
    print(Ka_b)
    print("SGT: ")
    print(SGT)
    Ka_bFile = open("./Ka_b.txt", "w+")
    Ka_bFile.write(str(Ka_b))

    SGTFile = open("./SGT.txt", "w+")
    SGTFile.write(SGT)
    return JsonResponse(data)

def connect(request):
    client_id = "Alice"
    server_id = "Bob"
    """
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    """

    time_stamp = time.time()
    lifetime = 600
    Ka_bFile = open("./Ka_b.txt", "r+")
    Ka_b = Ka_bFile.read()
    Ka_b = int(Ka_b)
    SGTFile = open("./SGT.txt", "r+")
    SGT = SGTFile.read()

    Auth = {
        "client_id": client_id,
        "client_address": "127.0.0.1",
        "time_stamp": time_stamp,
        "lifetime": lifetime
    }

    en_Auth = encrypt(Ka_b, str(Auth))
    keyword = {
        "en_Auth": en_Auth,
        "SGT": SGT
    }
    r = requests.post('http://127.0.0.1:8002/action/connect/', keyword)
    print(r.text)
    return HttpResponse(r)