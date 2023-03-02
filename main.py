# models.py

from django.db import models

class Policy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pattern = models.CharField(max_length=255)

class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=255)
    headers = models.TextField()
    data = models.TextField()
    result = models.TextField()

# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Policy, Log

def home(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        is_scripted = detect_scripted(data)
        if is_scripted:
            result = detect_xss(data)
        else:
            result = detect_sql_injection(data)
        log_request(request.method, request.build_absolute_uri(), request.headers, data, result)
        return HttpResponse(result)
    else:
        return render(request, 'home.html')

def detect_scripted(data):
    # Use regular expressions or other criteria to determine if the request is scripted
    return True

def detect_xss(data):
    # Use Content Security Policy (CSP) or other techniques to detect Cross-Site Scripting attacks
    return 'Possible XSS attack detected'

def detect_sql_injection(data):
    # Use parameterized queries or other techniques to detect SQL injection attacks
    return 'Possible SQL injection attack detected'

def log_request(method, url, headers, data, result):
    # Log the request details and detection results in the database
    log = Log(method=method, url=url, headers=headers, data=data, result=result)
    log.save()

# home.html

<!DOCTYPE html>
<html>
<head>
    <title>Injexa</title>
</head>
<body>
    <form method="post">
        <textarea name="data"></textarea>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
