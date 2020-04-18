from django.shortcuts import render
from .endecrypt import *
# Create your views here.
from django.http import HttpResponse,JsonResponse
import requests
import json
import socket
import time
Kb=45678

def connect(request):
    if request.method == 'POST':
        en_Auth = request.POST.get('en_Auth')
        SGT = request.POST.get('SGT')

    #获得ip
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    sgt = eval(decrypt(Kb,SGT))
    Ka_b = int(sgt["Ka_b"])
    Auth = eval(decrypt(Ka_b,en_Auth))

    print(sgt)
    print(Auth)
    if sgt["client_id"] == Auth["client_id"] and sgt["client_address"] == Auth["client_address"]:
        """
        reqdata = {
            "client_id":Auth["client_id"],
            "connection_situation":"welcome"
        }
        """
        return HttpResponse("welcome %s"%(Auth["client_id"]))
    else:
        return HttpResponse("Access Denied : %s"%(Auth["client_id"]))
