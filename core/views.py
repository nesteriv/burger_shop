from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from core.models import Category, Subcategory, Product


# Create your views here.
@login_required
def home(request):
    return redirect('/menu/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def show_menu (request):
    products = Product.objects.order_by('product_category', 'product_subcategory')
    categorys = Category.objects.all()
    subcategorys = Subcategory.objects.all()

    args = {}
    args['products'] = products
    args['categorys'] = categorys
    args['subcategorys'] = subcategorys

    return render(request, 'menu.html', args)
