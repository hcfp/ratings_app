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

    combined_names_data = []
    combined_names_data.append(data[0])
    del data[0]
    for item in data:
        is_unique = True
        for combined in combined_names_data:
            if combined["professor__code"] != item["professor__code"] and item["module__module__code"] == combined["module__module__code"] and item["module__module__name"] == combined["module__module__name"] and item["module__year"] == combined["module__year"]:
                combined["professor__code"] += " " + item["professor__code"]
                combined["professor__title"] += " " + item["professor__title"]
                combined["professor__first_name"] += " " + item["professor__first_name"]
                combined["professor__last_name"] += " " + item["professor__last_name"]
                is_unique = False
        if is_unique:
            combined_names_data.append(item)

    return JsonResponse({"list": combined_names_data})

@login_required
def view(request):
    data = []
    ratings_qs = Ratings.objects.values('score', 'professor__code', 'professor__title',
                                        'professor__first_name', 'professor__last_name')
    for row in ratings_qs:
        data.append(row)

    prof_ratings = {}
    for row in data:
        if row["professor__code"] not in prof_ratings:
            prof_ratings[row["professor__code"]] = [row["score"]]
        else:
            prof_ratings[row["professor__code"]].append(row["score"])
    average_prof_ratings = prof_ratings
    prof_average = {}
    for code, ratings in average_prof_ratings.items():
        average_prof_ratings[code] = round(sum(ratings) / len(ratings))
        if row["professor__code"] == code:
            prof_average["professor-title"] = row["professor__title"] 
            prof_average["professor-first-name"] = row["professor__first_name"]
            prof_average["professor-last-name"] = row["professor__last_name"]
            prof_average["module-code"] = code
            prof_average["average"] = average_prof_ratings[code]
            break
    print(prof_average, file=sys.stderr)

    return JsonResponse({"view": prof_average})


def average(request):
    data = []

    module_code = request.POST["module-code"]
    prof_code = request.POST["professor-code"]

    module_id = Module.objects.filter(code=module_code).values('id')
    prof_id = Professors.objects.filter(code=prof_code).values('id')
    module_instances = ModuleInstance.objects.filter(module__in=module_id).values('id')
    average_ratings = Ratings.objects.filter(module_instance__in=module_instances, professor__in=prof_id).values('module_instance__module__code', 'module_instance__module__name', 'professor__code', 'professor__title', 'professor__first_name', 'professor__last_name', 'score')
    
    for rating in average_ratings:
        data.append(rating)

    sum_data = 0
    for item in data:
        sum_data += int(item["score"])
    average_data = round(sum_data / len(data))
    return JsonResponse({"professor-title":data[0]["professor__title"], "professor-first-name":data[0]["professor__first_name"], "professor-last-name":data[0]["professor__last_name"], 'module-name':data[0]["module_instance__module__name"], 'average-score':average_data})


def rate(request):
    pass
