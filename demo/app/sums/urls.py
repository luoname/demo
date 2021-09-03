from django.urls import re_path
from . import views

urlpatterns = [
    re_path('add/', views.SUMAddView.as_view()),
    re_path('get_date/', views.GetDateView.as_view()),
]
