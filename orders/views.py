from django.shortcuts import render,redirect
from Authentication.models import Barista
import json
from orders.models import Order
def myOrders(request):
    if request.POST:
        order = Order.objects.filter(id=request.POST.get("ready"))
        order[0].delete()
        updateBaristas(-1)
    try:
        if request.user.client:
            orders = Order.objects.filter(client=request.user.client,alreadyPrepared=False)
            numOfOrders = len(orders)
            quantities = [json.loads(q.quatities) for q in orders]
            items = [json.loads(order.menuObjs) for order in orders]
            total = [order.total for order in orders]
    except:
        if request.user.barista or request.user.is_superuser:
            orders = Order.objects.filter(alreadyPrepared=False)
            numOfOrders = len(orders)
            quantities = [json.loads(q.quatities) for q in orders]
            items = [json.loads(order.menuObjs) for order in orders]
            total = [order.total for order in orders]
    return render(request,'Orders/myOrders.html',{'orders':orders,'items':items,'quantities':quantities,'size':range(0,numOfOrders),'total':total})

def PlaceOrder(request):
    if request.POST:
        quantities = request.POST.getlist("quatities")
        orders = request.POST.getlist("orders")
        totalPrice = request.POST.get("sum")
        payMethod = request.POST.get("method")
        updateBaristas(1)
        Order.objects.create(client=request.user.client,paymentMethod= payMethod,menuObjs=json.dumps(orders),quatities=json.dumps(quantities),total=totalPrice,alreadyPrepared=False)

    return redirect('/')


def updateBaristas(val):
    for barista in Barista.objects.all():
        barista.ordersToPrepare += val
        barista.save()