from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from core.models import Category, Subcategory, Product


# Create your views here.
def show_menu (request):
    products = Product.objects.order_by('product_category', 'product_subcategory')
    categorys = Category.objects.all()
    subcategorys = Subcategory.objects.all()

    args = {}
    args['products'] = products
    args['categorys'] = categorys
    args['subcategorys'] = subcategorys

    return render(request, 'menu.html', args)
