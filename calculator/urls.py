from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('hourcalc/', views.hourcalc, name = 'hour'),
    path('projectcalc/', views.projectcalc, name = 'project')
]