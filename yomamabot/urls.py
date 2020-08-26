# yomamabot/yomamabot/urls.py
from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fb_yomamabot/', include('fb_yomamabot.urls')),
]

# localhost:8000/fb_yomamabot/