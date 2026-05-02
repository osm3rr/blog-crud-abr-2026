from django.urls import path
from .views import (ArticleListView,
                    ArticleDetailView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleDeleteView
                    )

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('articulo/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articulo/crear/', ArticleCreateView.as_view(), name='article-create'),
    path('articulo/<int:pk>/editar/', ArticleUpdateView.as_view(), name='article-update'),
    path('articulo/<int:pk>/eliminar/', ArticleDeleteView.as_view(), name='article-delete'),
]