from django.urls import path, include

from apps.mainapp import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
]
