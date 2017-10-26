from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView
  

    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    url(r'^(?P<pk>\d+)/edit/$', CommentUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', CommentDeleteAPIView.as_view(), name='delete'),
]