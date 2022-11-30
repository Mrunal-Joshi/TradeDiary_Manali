from django.shortcuts import render
from TradeSheet.models import TradeSheet
from django.http import HttpResponse
import plotly.express as px
import pandas as pd
# Create your views here.

def tradeAnalysis(request):
    sheet=TradeSheet.objects.all().values()
    df = pd.DataFrame(sheet)
    print(df)

    pie_chart = px.pie( df, values='no_of_shares', names='symbol')
    pie_chart=pie_chart.to_html()

    line_chart = px.line(df,x="date", y="no_of_shares")
    line_chart=line_chart.to_html()


    return render(request,'analysis.html',{'pie_chart':pie_chart,'line_chart':line_chart})

