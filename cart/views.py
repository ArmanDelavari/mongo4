from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart  # yek nemune azash sakhte mishe initesh faal mishe yek session be name cart sakhte mishe
from .forms import CartAddForm


# Create your views here.
def detail(request):
    cart = Cart(request)  # unvar too cart bebinid initesh request dare dg pas too nemunash inja bas behesh bedim
    return render(request, 'cart/detail.html', {'cart': cart})


@require_POST  # in kheili vajebe nmige faghat az tarighe post begir
def cart_add(request, product_id):  # etelaaat ke az html shop bam etode post dadim be url in az in mifresim be cart.py
    cart = Cart(request)  # darkhastai ke miad ro mirizm tooye class Cart va zakhire mikonim tooye in motaghayer
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, tedad=cd['tedad'])  # hamun chizhai ke mifreste be class cart dar cart.py
    return redirect('cart:detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')
