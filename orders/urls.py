from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.oerder_create, name='create'),
    path('<int:order_id>/', views.detail, name='detail'),

    # zarin ball
    path('payment/<int:order_id>/<price>/', views.payment, name='payment'),  # 1  prico mifresim, int order id baraye ineke
    # vaghti pardakht movafagh bud mikhaym berim too modele order va pay ro true konim ke yani pardakht anjam shode age na lazem nabud
    path('verify/', views.verify, name='verify'),  # 2
]
