from django.urls import path
from information import views,forms
from information.views import information,informationTest,information_model

urlpatterns = [
    path('information/', views.FormView.as_view(), name='information'),
    path('informationTest/', views.FormView.as_view(), name='informationTest'),
    path('information_model/', views.FormView.as_view(), name='information_model'),  
]