from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CodeForm
from .models import Order, Order_item
from cart.cart import Cart
from suds.client import Client

@login_required
def detail(request, order_id):
    form = CodeForm()
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/orders.html', {'order': order, 'form': form})


@login_required
def oerder_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        Order_item.objects.create(order=order, product=item['product'], price=item['price'], tedad=item['tedad'])
        cart.clear()
    return redirect('orders:detail', order.id)


# zarin ballll


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'   # hamun code ke goftim noghrei shim tooye zarin bal behemun mide
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')   # maro be un dargah mibare
description = "پرداخت مونگارد"   # tozihati ke mikhahim
mobile = '09123456789'   # imael va mobile karbari ke kharid kardeo midim in khubish ine residi ke zarin bal behemun mide inaro toosh hack mikone
# email = 'abasgholi@yahoo.com'  # agar nadashtim ke hichi khali mizarim  pain tarifesh mikonim mobilam mese hamin mishod agar mikhasim
# agar mobile ya email harkodum ro nadashtim inja be soorate fake ye chizi bayad ghar bedim
CallbackURL = 'http://localhost:8000/orders/verify/'   # bade inke bargasht kharid shod koja bere

# in dota metod hefzie
# ma aghat chizai je fargh dare too har prozhe roo minevisim
@login_required
def payment(request, order_id, price):  # prico migire,   order id ro too url tozih dadim chera mihaym
    global amount, o_id   # o_id az khodemun darovordim  nemishe hamun order_id gozasht hala mishe raft tpoo tabeye pain azash estefade kard
    amount = price
    o_id = order_id
    result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)   # request.user.email hamunek eb la gofitm0
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))   # avalish in agar natunes bere too safheye pardakht be har dalili in
#     ye error mide say komid ye safhe tarahi konid ke ye messages ghashang bede na mese in zayas


@login_required
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            # agar movafaght bud bia
            order = Order.objects.filter(id=o_id)   # in ro begir
            order.paid = True   # inro too model True kon
            order.save()
            messages.success(request, 'Transaction was successful', 'success')
            return redirect('shop:home')
        elif result.Status == 101:
            return HttpResponse('Transaction submitted')   # in ghablan anham shode mitunim hameye in http haro taghir bedim
        else:
            return HttpResponse('Transaction failed.')   # tarakonesh na movafagh
    else:
        return HttpResponse('Transaction failed or canceled by user')   # tarakonesh na movafagh ya tavasote karbar laghv shode ast
