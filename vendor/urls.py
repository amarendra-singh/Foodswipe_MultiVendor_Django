from django.urls import path, include
from accounts import views as AccountViews
from . import views


urlpatterns = [
    path ('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', views.profile, name='profile'),
]