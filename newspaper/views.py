from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView,
                                )
from .models import Article

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