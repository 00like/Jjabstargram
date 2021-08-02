# from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings

from membercheck import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login, name='membercheck_check'),
]