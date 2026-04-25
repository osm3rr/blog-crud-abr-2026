from django.urls import path
from .views import (ArticleListView,
                    ArticleDetailView,
                    ArticleCreateView,
                    )

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('articulo/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articulo/crear/', ArticleCreateView.as_view(), name='article-create'),
]