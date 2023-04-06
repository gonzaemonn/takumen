from django.urls import path
from information import views
from information.views import information,informationTest,information_model

urlpatterns = [
    path('information/', information, name='information'),
    path('informationTest/', informationTest, name='informationTest'),
    path('information_model/', information_model, name='information_model'),  
]