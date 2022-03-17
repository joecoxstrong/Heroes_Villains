from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.Super),
    path('<int:pk>/', views.Super)
]

urlpatterns = format_suffix_patterns(urlpatterns)