from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddForm



def home(request, slug=None):  # tooye url bebinid dota url dare miad be be in tabe ekish slug dare yekish nadare
    # agar none nazarim uni ke slug nadare mige chera slug dadi ghati mikone amma inja migim nono bede besh ke un error nade
    products = Product.objects.all()
    categories = Category.objects.filter(is_sub=False)  # migim unai ke zir daste bandi nistan kollian
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = CartAddForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})
