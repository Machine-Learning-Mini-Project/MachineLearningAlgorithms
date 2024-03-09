from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def copyleaksComp(request):

    if (request.method == "POST"):
        payload = json.loads(request.body)
        print(payload['results']['score'])

    return HttpResponse()

def copyleaksErr(request):
    return HttpResponse()

@csrf_exempt
def copyleaksCheck(request):
    if (request.method == "POST"):
        payload = json.loads(request.body)
        print(payload['credits'])

    return HttpResponse()