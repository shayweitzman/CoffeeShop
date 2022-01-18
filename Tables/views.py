from django.shortcuts import render


def order(request):
    return render(request, 'Tables/orderTable.html')
