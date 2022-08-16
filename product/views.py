# Create your views here.
from product.form import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import product
from product.models import Category


class ListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'title': 'Products', 'page_title': 'Product List'}
        return render(request, 'product/index.html', context)

class AddView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'title': 'Add Product', 'page_title': 'Add Product'}
        context['form'] = ProductForm()
        return render(request, 'product/add.html', context)



#Manage Categories
class CategoryListView(LoginRequiredMixin, View):
    def get(self, request, id=False):
        categories = Category.objects.order_by('-id')
        context = {'title': 'Categories', 'page_title': 'Product Categories', 'categories': categories}
        return render(request, 'product/category/index.html', context)

    def post(self, request):
        categoryName = request.POST['name'].strip()
        parentCat = 0
        errorMessage = None

        if (not categoryName):
             errorMessage = 'Category Name is required.'
        elif len(categoryName) < 4:
             errorMessage = 'Category Name is required.'

        if not errorMessage:
             newCategory = Category(name=categoryName, parent=parentCat)
             newCategory.save()
             messages.add_message(request, messages.SUCCESS, 'New category Successfully added')
        else:
            messages.add_message(request, messages.WARNING, errorMessage)
        return redirect('/product/categories')

class CategoryEditView(LoginRequiredMixin, View):
    def get(self, request, id):

        categories = Category.objects.order_by('-id')

        context = {'title': 'Edit Category', 'page_title': 'Product Categories', 'categories': categories}
        context['category_id'] = id
        context['single_category'] = get_object_or_404(Category, pk=id)

        return render(request, 'product/category/index.html', context)

    def post(self, request, id):
        categoryName = request.POST['name'].strip()
        categoryStatus = request.POST['status']

        parentCat = 0
        errorMessage = None

        if (not categoryName):
             errorMessage = 'Category Name is required.'
        elif len(categoryName) < 4:
             errorMessage = 'Category Name is required.'

        if not errorMessage:
             updateCat = Category(id=id,name=categoryName, parent=parentCat, status=categoryStatus)
             updateCat.save()
             messages.add_message(request, messages.SUCCESS, 'Category Successfully Updated')
        else:
            messages.add_message(request, messages.WARNING, errorMessage)
        return redirect('/product/categories')

class CategoryDeleteView(LoginRequiredMixin, View):

    def get(self, request, id):
        Category.objects.filter(id=id).delete()
        messages.add_message(request, messages.SUCCESS, 'Category Successfully Deleted')
        return redirect('/product/categories')



