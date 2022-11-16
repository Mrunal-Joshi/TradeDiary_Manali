from django.shortcuts import render
from django.http import HttpResponse

from .models import TradeSheet
# Create your views here.
def displaysheet(request):
    sheet = 
    return render(request,'tradesheet.html')