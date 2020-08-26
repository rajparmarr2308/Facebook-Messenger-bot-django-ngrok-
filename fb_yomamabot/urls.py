# yomamabot/fb_yomamabot/urls.py
from django.conf.urls import include, url
from .views import YoMamaBotView
urlpatterns = [
    url(r'^7a080d34747afd2aa9ad88c429a3e775cffe526b485e813057/?$', YoMamaBotView.as_view()) 
        ]