from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TradeSheet
from .forms import TradeSheetForm
from django.contrib import messages


def displaysheet(request):
    # <QuerySet [{'id': 1, 'date': datetime.date(2022, 11, 16), 
    # 'symbol': 'FISV', 'no_of_shares': 12, 'buy_price': 110.0, 'sell_price': 11.0, 'profit_loss': 0.0}
    if request.method == "POST":
        form = TradeSheetForm(request.POST or None)
        
        if form.is_valid():           
            form.save()
            messages.success(request, ("Trade Added!s"))
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)

        return redirect('tradesheet')

    else:   
        sheet = TradeSheet.objects.all().values()
        return render(request,'tradesheet.html',{'sheet':sheet})


def editTrade(request,id):
    #if request.method == "POST":
    TradeSheet.objects.filter(id=id).delete()      
    return redirect('tradesheet')

def deleteTrade(request,id):
    TradeSheet.objects.filter(id=id).delete()
    sheet = TradeSheet.objects.all().values()
    #messages.success(request, ("Trade Deleted!"))
    return redirect('tradesheet')
    #return render(request,'tradesheet.html',{'sheet':sheet}) 