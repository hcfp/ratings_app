from re import S
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
import json
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from isort import file
from .models import Professors, Ratings, ModuleInstance, Module, ModuleLeaders


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    return JsonResponse({'username': username, 'email': email, 'register-success': True})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return JsonResponse({'username': username, 'login-success': True})
    else:
        return JsonResponse({'username': username, 'login-success': False})


def logout(request):
    auth_logout(request)
    return JsonResponse({'logout-success': True})


@login_required
def list_all(request):
    data = []
    module_leaders_qs = ModuleLeaders.objects.values('module__module__code', 'module__module__name', 
                                                    'module__year', 'module__semester', 
                                                    'professor__code', 'professor__title',
                                                    'professor__first_name', 'professor__last_name')

    for row in module_leaders_qs:
        data.append(row)

    return JsonResponse({"list": data})

#@login_required
def view(request):
    data = []
    ratings_qs = Ratings.objects.values('score', 'professor__code', 'professor__title',
                                        'professor__first_name', 'professor__last_name')
    for row in ratings_qs:
        data.append(row)

    return JsonResponse({"view": data})


def average(request):
    pass


def rate(request):
    pass
