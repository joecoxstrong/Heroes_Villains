from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.SuperList),
    path('<int:pk>/', views.SuperDetail),
    path('supers?type=<type>/', views.SuperList)
]

urlpatterns = format_suffix_patterns(urlpatterns)