from django.urls import path
from . import views

urlpatterns = [
    path('simple/position=<str:position>&size=<str:size>/', views.simpleConversion),
    path('advanced/xPos=<int:xPos>&yPos=<int:yPos>&size=<str:size>/', views.advancedConversion),
    path('download/', views.download)
]