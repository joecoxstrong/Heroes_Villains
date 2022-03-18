from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.SuperTypesList),
    path('<int:pk>/', views.SuperTypeDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)