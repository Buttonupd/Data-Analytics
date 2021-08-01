from Visualize.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls import static, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('powerDjango.urls'))
]

