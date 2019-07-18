#Middleware 1
class LoginMiddleware(object):

    def __init__(self,get_response):
        self.get_response  = get_response

    def __call__(self,request):
        print("This line is printed at pre-procesing Request")
        response = self.get_response(request)
        print("This line is printed at post-procesing request")
        return response

#Middleware 2:
from django.http import HttpResponse

class AppMaintenceMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        return HttpResponse("<h1>This Application is Undermaintence ....Please Visit After 2PM Today!!!!!!")

    def process_exception(self,request,exception):
        print("<h1>This Application Under Maintenance")

#Middleware3:
class ExceptionMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s1 = "<h1><bg color:red>We are facing Some Technical Issue ....We will come back Soon!! Thanks For Visiting This App</bg><h1>"
        return HttpResponse(s1)







