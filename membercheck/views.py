from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        target_username = data['username']
        target_password = data['password']              
        
        login_result = authenticate(username=target_username, password=target_password)
        if login_result:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=401)
                
        # if target_username and target_password:
        #     try:
        #         obj = User.objects.get(username=target_username)
        #     except User.DoesNotExist:                            
        #         return HttpResponse(status=401)
        
        # if(obj.check_password(target_password) == True):             
        #     return HttpResponse(status=200)
        # else:
        #     return HttpResponse(status=401)
       
        
        
    