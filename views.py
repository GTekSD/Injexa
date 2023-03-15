import re
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Policy, Log

def home(request):
    policies = Policy.objects.all()
    context = {
        'policies': policies
    }
    return render(request, 'home.html', context)

@csrf_exempt
def detect_scripted(request):
    policies = Policy.objects.all()
    result = 'OK'
    for policy in policies:
        pattern = policy.pattern
        if re.search(pattern, request.body.decode('utf-8')):
            result = 'Detected'
            break
    log = Log.objects.create(
        method=request.method,
        url=request.build_absolute_uri(),
        headers=request.headers,
        data=request.body.decode('utf-8'),
        result=result
    )
    return HttpResponse(status=200)

@csrf_exempt
def detect_xss(request):
    result = 'OK'
    if '<script>' in request.body.decode('utf-8'):
        result = 'Detected'
    log = Log.objects.create(
        method=request.method,
        url=request.build_absolute_uri(),
        headers=request.headers,
        data=request.body.decode('utf-8'),
        result=result
    )
    return HttpResponse(status=200)

@csrf_exempt
def detect_sql_injection(request):
    result = 'OK'
    if 'SELECT' in request.body.decode('utf-8'):
        result = 'Detected'
    log = Log.objects.create(
        method=request.method,
        url=request.build_absolute_uri(),
        headers=request.headers,
        data=request.body.decode('utf-8'),
        result=result
    )
    return HttpResponse(status=200)
