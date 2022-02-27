from re import S
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
import json
from django.contrib.auth import login
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
        print("test",file=sys.stderr)
        user = User.objects.create_user(data["username"], data["email"], data["password"])
        user.save()
    except:
        pass
    return JsonResponse(data)