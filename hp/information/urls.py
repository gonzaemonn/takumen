from django.urls import path
from information import views
from information.views import information,informationTest

urlpatterns = [
    path('information/', information, name='information'),
    path('informationTest/', informationTest, name='informationTest'),
]