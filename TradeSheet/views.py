from django.shortcuts import render
from django.http import HttpResponse

from .models import TradeSheet
# Create your views here.
def displaysheet(request):
    # <QuerySet [{'id': 1, 'date': datetime.date(2022, 11, 16), 
    # 'symbol': 'FISV', 'no_of_shares': 12, 'buy_price': 110.0, 'sell_price': 11.0, 'profit_loss': 0.0}
    sheet = TradeSheet.objects.all().values()
    # for i in sheet:
    #     print(i['profit_loss']=i['sell_price']-i['buy_price'])

    return render(request,'tradesheet.html',{'sheet':sheet})