from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.SuperList.as_view()),
    path('<int:pk>/', views.SuperList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)