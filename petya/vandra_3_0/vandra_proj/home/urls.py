from django.urls import path


from home.views import PostListView, ArticleDetailView

urlpatterns = [
    # path('', views.home, name='home')
    path('', PostListView.as_view(), name='home'),
    path('articles/<slug:slug>', ArticleDetailView.as_view(), name='article-detail')
]