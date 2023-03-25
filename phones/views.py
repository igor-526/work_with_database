from django.shortcuts import render, redirect, HttpResponse
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': []}
    sort = request.GET.get("sort")
    if sort == "name":
        phones = Phone.objects.all().order_by('name')
    elif sort == "min_price":
        phones = Phone.objects.all().order_by('price')
    elif sort == "max_price":
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    for phone in phones:
        context['phones'].append(phone)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {"phone": phone[0]}
    return render(request, template, context)