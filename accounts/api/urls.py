from django.conf.urls import url
from django.contrib import admin

from rest_framework.authtoken import views

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    #url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^sign-up/$', UserCreateAPIView.as_view(), name='signup'),
    url(r'^auth-token/$', views.obtain_auth_token, name='get_auth_token'),
]