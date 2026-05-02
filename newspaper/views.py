from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
                                )
from .models import Article
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles-list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article-detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article-create.html'
    fields = ['title', 'content', 'author']

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article-update.html'
    fields = ['title', 'content']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article-delete.html'
    success_url = reverse_lazy('article-list')