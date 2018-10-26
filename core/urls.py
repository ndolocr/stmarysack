from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.home, name='admin-home')
]

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''