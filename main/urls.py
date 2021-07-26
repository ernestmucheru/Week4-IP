from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('all-hoods/', views.hoods, name='hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('new-hood/', views.create_hood, name='new-hood'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
