from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name ="login"),
    path('signup/', Signup.as_view(), name="signup"),
    path('logout/', Logout , name="logout"),
    path('details/', Details.as_view(), name="details"),
    path('details/<int:pk>', Details.as_view(), name="details_of_comp"),
    path('add/', Add.as_view(), name="add"),
    path('profile/', Profile.as_view(), name="profile"),
    path('ipocheck/', Ipocheck.as_view(), name="ipocheck"),
    path('edit/', EditBoid.as_view(), name='editboid'),

]