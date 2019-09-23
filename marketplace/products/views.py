from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404

from .forms import ProductForm
from .models import Product, Category


def get_instance(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404


def home(request):
    products = Product.objects.all()[:5]
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)


def products_with_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


class ProductView(View):
    model = Product

    def get(self, request, *args, **kwargs):
        context = {}
        if kwargs.get('pk') is not None:
            product = get_instance(self.model, kwargs.get('pk'))
            context['product'] = product
            return render(request, 'products/product.html', context)
        else:
            products = self.model.objects.all()
            context['products'] = products
        return render(request, 'products/products.html', context)


class ProductForm(View):
    """
        GET, POST, PUT and DELETE
    """
    model = Product
    form_cls = ProductForm

    def get(self, request, *args, **kwargs):
        context = {}
        if kwargs.get('pk') is not None:
            product = get_instance(self.model, kwargs.get('pk'))
            form = self.form_cls(instance=product)
            context['form'] = form
        else:
            form = self.form_cls()
            context['form'] = form
        return render(request, 'products/form.html', context)

    def post(self, request, *args, **kwargs):
        '''
            Create new product if pk is None else update it
        '''
        # Create a form instance with the submitted data
        if kwargs.get('pk') is not None:
            product = get_instance(self.model, kwargs.get('pk'))
            form = self.form_cls(request.POST or None, instance=product)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
            return redirect(product.get_absolute_url())
        form = self.form_cls(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        return redirect('/')
