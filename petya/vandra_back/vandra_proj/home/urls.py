from django.urls import path
from . import views
# from .views import HomeView

urlpatterns = [
    # path('', views.home, name='home')
    path('', views.home, name='home'),
]