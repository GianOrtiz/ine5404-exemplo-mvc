from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.StockView.as_view(), name='index'),
    path('products/add', views.ProductCreateView.as_view(),
        name='products-add'),
    path('products/<int:pk>/detail',
        views.ProdutDetailView.as_view(), name='products-detail'),
    path('products/<int:pk>/delete',
        views.ProductDeleteView.as_view(), name='products-delete'),
    path('products/<int:pk>/update',
        views.ProductUpdateView.as_view(), name='products-update'),
]