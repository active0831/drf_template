from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('yoururl/<int:pk>/',YourView.as_view()), ### [ Modify this ] ###
]
urlpatterns = format_suffix_patterns(urlpatterns)
