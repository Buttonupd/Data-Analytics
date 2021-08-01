from django.conf.urls import url
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', classify_review, name='classify_review'),
    url('thanks', feedback, name='feedback')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)