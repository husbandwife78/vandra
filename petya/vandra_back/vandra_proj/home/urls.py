from django.urls import path
from . import views
from home.views import PostListView

urlpatterns = [
    # path('', views.home, name='home')
    path('', PostListView.as_view(), name='home'),
]