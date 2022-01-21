from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import TableOrder, Table
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


def createOrder(request, table_id, time, date):
    table = get_object_or_404(Table, pk=table_id)
    try:
        TableOrder.objects.create(clients=request.user.client, tables=table, time=time,
                                  date=date.split('/')[2] + '-' + date.split('/')[0] + '-' + date.split('/')[1])
    except:
        return 0
    return 1


def order(request):
    date1 = datetime.datetime.today()
    time = datetime.time(datetime.datetime.today().hour + 1)
    if "reserved" in request.POST:
        if (
        not createOrder(request, request.POST.get("reserved"), request.POST.get("time1"), request.POST.get("date"))):
            return render(request, 'Tables/orderTable.html',
                          { 'time': "Table Already Taken!"})
        else:
            return render(request, "Tables/table_resevation.html",
                          {'table': get_object_or_404(Table, pk=request.POST.get("reserved")),
                           "time": request.POST.get("time1"), "date": request.POST.get("date")})
    elif request.POST:
        try:
            date1 = datetime.datetime.strptime(request.POST.get("datepicker"), "%m/%d/%Y")
            time = datetime.time(int(request.POST.get("time")))
        except:
            return render(request, 'Tables/orderTable.html',
                          {'date': date1.strftime("%m/%d/%Y"), 'time': "please chose valid date"})
    orders = list(TableOrder.objects.filter(date=date1))
    orders = list(filter(lambda x: x.time.hour == time.hour, orders))
    occupiedT = []
    for i in orders:
        occupiedT.append(i.tables)
    freeTabels = []
    if date1.strftime("%A") != 'Friday' and date1.strftime("%A") != 'Saturday':
        freeTabels = list(Table.objects.filter(~Q(UnavailabDay=date1.strftime("%A"))))
        freeTabels = list(filter(lambda x: x not in occupiedT, freeTabels))
    if date1.date() < datetime.datetime.today().date():
        return render(request, 'Tables/orderTable.html',
                      {'date': date1.strftime("%m/%d/%Y"), 'time': "please chose valid date"})
    elif date1.date() == datetime.datetime.today().date() and time.hour <= datetime.datetime.today().hour:
        return render(request, 'Tables/orderTable.html',
                      {'date': date1.strftime("%m/%d/%Y"), 'time': "please chose valid time"})
    else:
        return render(request, 'Tables/orderTable.html',
                      {'tables': freeTabels, 'date': date1.strftime("%m/%d/%Y"), "time": time.strftime("%H:%M")})