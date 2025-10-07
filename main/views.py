from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

#Tugas 4
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse #Tugas 5
from django.urls import reverse

#Tugas 5
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    category = request.GET.get("category", "")  # get category filter
    
    # Base queryset
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    # Apply category filter if specified
    if category:
        product_list = product_list.filter(category=category)

    context = {
        'name': 'I Gusti Ngurah Agung Airlangga Putra',
        'npm' : '2406358794',
        'class': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')

    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'name': 'I Gusti Ngurah Agung Airlangga Putra',
        'npm' : '2406358794',
        'class': 'PBP F',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        rating_value = request.POST.get("rating")
        try:
            rating_float = float(rating_value)
            if rating_float < 0:
                rating_float = 0.0
            if rating_float > 5:
                rating_float = 5.0
            product.rating = rating_float
            product.save()
            return redirect('main:show_product', id=product.id)
        except (TypeError, ValueError):
            pass
    product.increment_views()

    context = {
        'product': product,
        'name': 'I Gusti Ngurah Agung Airlangga Putra',
        'npm' : '2406358794',
        'class': 'PBP F',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "product_detail.html", context)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.select_related('user').all()
    category = request.GET.get('category')
    filter_type = request.GET.get('filter')  # 'all' or 'my'
    if category:
        product_list = product_list.filter(category=category)
    if filter_type == 'my' and request.user.is_authenticated:
        product_list = product_list.filter(user=request.user)
    data = [
        {
            'id': str(p.id),
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'product_views': p.product_views,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'is_featured': p.is_featured,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user_id else None,
            'brand': p.brand,
            'weight': p.weight,
            'rating': p.rating,
        }
        for p in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        p = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(p.id),
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'product_views': p.product_views,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'is_featured': p.is_featured,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user_id else None,
            'brand': p.brand,
            'weight': p.weight,
            'rating': p.rating,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

# Tugas 4   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect_url': f"{reverse('main:login')}?registered=1"})
            messages.success(request, 'Your account has been successfully created!')
            return redirect(f"{reverse('main:login')}?registered=1")
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                resp = JsonResponse({'success': True, 'redirect_url': f"{reverse('main:show_main')}?loggedin=1"})
                resp.set_cookie('last_login', str(datetime.datetime.now()))
                return resp
            response = HttpResponseRedirect(f"{reverse('main:show_main')}?loggedin=1")
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)


   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(f"{reverse('main:login')}?loggedout=1")
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        updated = form.save()
        # AJAX support
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'id': str(updated.id),
                'name': updated.name,
                'price': updated.price,
                'description': updated.description,
                'category': updated.category,
                'thumbnail': updated.thumbnail,
                'is_featured': updated.is_featured,
                'brand': updated.brand,
                'weight': updated.weight,
                'rating': updated.rating,
            })
        return redirect('main:show_main')

    context = {
        'form': form,
        'name': 'I Gusti Ngurah Agung Airlangga Putra',
        'npm' : '2406358794',
        'class': 'PBP F',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'deleted'})
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name", ""))
    description = strip_tags(request.POST.get("description", ""))
    price_raw = request.POST.get("price", "0")
    try:
        price = int(float(price_raw))
    except (TypeError, ValueError):
        price = 0
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    brand = request.POST.get("brand", "")
    weight_raw = request.POST.get("weight", "0")
    try:
        weight = int(float(weight_raw))
    except (TypeError, ValueError):
        weight = 0
    is_featured = request.POST.get("is_featured") in ["on", "true", "1", True]

    product = Product(
        name=name,
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        brand=brand,
        weight=weight,
        is_featured=is_featured,
        user=request.user if request.user.is_authenticated else None,
    )
    product.save()

    return JsonResponse({
        'id': str(product.id),
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category': product.category,
        'thumbnail': product.thumbnail,
        'brand': product.brand,
        'weight': product.weight,
        'is_featured': product.is_featured,
    }, status=201)