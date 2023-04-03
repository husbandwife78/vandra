from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# def home(request):
#     return render(request, 'main_page.html')


class PostListView(ListView):
    model = Post
    template_name = 'main_page.html'

    # def  get_queryset(self):
    #     return Post.objects.
