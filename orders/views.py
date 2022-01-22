from django.shortcuts import render, redirect
from Authentication.models import Barista
from Menu.models import MenuObj
import json
from orders.models import Order
from Tables.models import TableOrder
import datetime
from .forms import TableOrderForm
from django.shortcuts import get_object_or_404


def myOrders(request):
    if request.POST:
        order = Order.objects.filter(id=request.POST.get("ready"))
        order[0].delete()
        updateBaristas(-1)
    try:
        if request.user.client:
            orders = Order.objects.filter(client=request.user.client, alreadyPrepared=False)
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
    return render(request, 'Orders/myOrders.html',
                  {'orders': orders, 'items': items, 'quantities': quantities, 'size': range(0, numOfOrders),
                   'total': total})


def TableOrders(request):
    orders = list(TableOrder.objects.all())
    orders = list(filter(lambda x: x.date > datetime.date.today(), orders))
    return render(request, 'orders/tableOrders.html', {'orders': orders})


def editTorder(request, table_id):
    currentOrder = get_object_or_404(TableOrder, pk=table_id)
    if request.method == "GET":
        return render(request, "Orders/editTableOrder.html", {"form": TableOrderForm(instance=currentOrder)})
    elif request.method == "POST":
        if "delete" in request.POST:
            TableOrder.delete(currentOrder)
            return redirect("table_orders")
        else:
            form = TableOrderForm(request.POST)
            if form.is_valid():
                TableOrder.delete(currentOrder)
                newOrder = form.save(commit=False)
                newOrder.save()
                return redirect("table_orders")
    return redirect("table_orders")


def PlaceOrder(request):
    if request.POST:
        quantities = request.POST.getlist("quatities")
        orders = request.POST.getlist("orders")
        totalPrice = request.POST.get("sum")
        payMethod = request.POST.get("method")
        updateBought(orders, quantities)

        updateBaristas(1)
        Order.objects.create(client=request.user.client, paymentMethod=payMethod, menuObjs=json.dumps(orders),
                             quatities=json.dumps(quantities), total=totalPrice, alreadyPrepared=False)
    return redirect('/')


def updateBought(orders, quantities):
    for (objName, quantity) in zip(orders, quantities):
        menuObj = MenuObj.objects.filter(name=objName)[0]
        menuObj.bought += int(quantity)
        menuObj.save()


def updateBaristas(val):
    for barista in Barista.objects.all():
        barista.ordersToPrepare += val
        barista.save()
