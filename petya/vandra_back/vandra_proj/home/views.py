from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# def home(request):
#     return render(request, 'test.html')

class HomeView(ListView):
    model = Post
    template_name = 'home_page.html'
