from django.shortcuts import render
from .endecrypt import *
# Create your views here.
from django.http import HttpResponse,JsonResponse
import requests
import random
import time
key={"AS":12345,"TGS":23456,"Alice":34567,"Bob":45678}
def givetgt(request):
    if request.method == 'POST':
        client_id  = request.POST.get('client_id')  # 获取clinet_id
        service_id = request.POST.get('service_id')  # 获取service_id

    Ka_tgs = random.randint(0,999999)
    print("Ka_tgs: ")
    print(Ka_tgs)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    print("ip: ")
    print(ip)

    time_stamp = time.time()
    lifetime = 600
    tgt={
        "client_id":client_id,
        "client_address":ip,
        "service_id":service_id,
        "time_stamp":time_stamp,
        "lifetime":lifetime,
        "Ka_tgs":Ka_tgs
    }
    en_Ka_tgs = encrypt(key[client_id],str(Ka_tgs))
    TGT = encrypt(key["TGS"],str(tgt))
    en_TGT = encrypt(key[client_id],TGT)

    reqdata = {"en_Ka_tgs":en_Ka_tgs,"en_TGT":en_TGT}

    print("tgt: ")
    print(str(tgt))
    print("en_TGT: ")
    print(en_TGT)

    return JsonResponse(reqdata)
    #return HttpResponse("Hello, world. You're at the action give-tgt.")


def givesgt(request):
    if request.method == 'POST':
        en_Auth = request.POST.get('en_Auth')
        TGT = request.POST.get('TGT')

    #获得ip
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    tgt = eval(decrypt(key["TGS"],TGT))
    Ka_tgs = int(tgt["Ka_tgs"])
    Auth = eval(decrypt(Ka_tgs,en_Auth))
    server_id = Auth["server_id"]
    if tgt["client_id"]==Auth["client_id"] and tgt["client_address"]==Auth["client_address"]:
        Ka_b = random.randint(0, 999999)
        time_stamp = time.time()
        lifetime = 600
        en_Ka_b = encrypt(Ka_tgs,str(Ka_b))
        sgt = {
            "client_id":Auth["client_id"],
            "client_address": Auth["client_address"],
            "time_stamp": time_stamp,
            "lifetime": lifetime,
            "Ka_b": Ka_b
        }
        SGT = encrypt(key[server_id],str(sgt))
        print("Ka_b: ")
        print(Ka_b)
        print("SGT: ")
        print(SGT)
        en_SGT = encrypt(Ka_tgs,SGT)
        reqdata = {
            "en_Ka_b":en_Ka_b,
            "en_SGT":en_SGT
        }
    return JsonResponse(reqdata)