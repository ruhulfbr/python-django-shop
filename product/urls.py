from django.urls import path
from .views import ListView, AddView, CategoryListView, CategoryEditView, CategoryDeleteView

from . import views

urlpatterns = [
    path('', ListView.as_view(), name="products"),
    path('create', AddView.as_view(), name="product.add"),

    path('categories', CategoryListView.as_view(), name="product-categories"),
    path('category/edit/<int:id>', CategoryEditView.as_view(), name="category.edit"),
    path('category/delete/<int:id>', CategoryDeleteView.as_view(), name="category.delete"),

]
