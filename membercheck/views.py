from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

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
        
        if target_username and target_password:
            try:
                obj = User.objects.get(username=target_username)
            except User.DoesNotExist:                            
                return HttpResponse(status=400)
        
        if(obj.check_password(target_password) == True):             
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
       
        
        
    