from decimal import Decimal

from shop.models import Product

CART_SESSION_ID = 'cart'  # midimesh be pain


class Cart:
    def __init__(self, request):
        self.session = request.session  # tamame seccion hai ke az tarafe site ma tooye morurgare karvar zakhire shode r aberiz too self.session
        cart = self.session.get(CART_SESSION_ID)  # az in session ha unai ro begir ke marbut be sabade kharide ma hastan
        if not cart:  # agar sabade kharid khali bud
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart  # zakhirash mikonim

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['tedad']  # be khatere zarinal dg decimal nemishe gozasht int mizarim
            yield item

    def add(self, product,
            tedad):  # product va tedad ro behesh midim ke dar view shop hastan, in dota meghdar vasash miad az unvar az view.py def cart._Add
        product_id = str(product.id)  # hatman be soorate str bayad zakhire she

        if product_id not in self.cart:  # agar az ghabl tooye sabade kharid nabud
            self.cart[product_id] = {'tedad': 0, 'price': str(product.price)}
        self.cart[product_id][
            'tedad'] += tedad  # migim dar gheire in soorat tedade barabare tedadi ke tooo parantez dare miad bokon
        self.save()

    def save(self):
        self.session.modified = True  # inam vajebe

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(int(item['price']) * item['tedad'] for item in self.cart.values())   # agar int nabashe zarin pal error migire

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()
