from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def m1(request):
    print("This one printed ofter pre-proccesing")
    print(10/0)
    s = "<h1>Middleware Project</h1>"
    return HttpResponse(s)



