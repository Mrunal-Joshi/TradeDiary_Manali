import plotly.express as px
import pandas as pd


def pie_chart(df):
    pie_chart = px.pie( df, values='no_of_shares', names='symbol')
    pie_chart=pie_chart.to_html()
    return pie_chart

def line_chart(df):
    line_chart = px.line(df,x="date", y="no_of_shares")
    line_chart=line_chart.to_html()
    return line_chart

def chart_win_by_trade(df):
    profit_count=df.loc[df['profit_loss']>0,'profit_loss'].count()
    #Analysis_data['win_rate']=profit_count*100//len(df)
    #print(df)
    pie_chart = px.pie( df, values='no_of_shares', names='symbol',width=300, height=300)
    pie_chart=pie_chart.to_html()
    return pie_chart

def chart_win_by_day(df):
    ## group by days -- wins VS losses
    test=df.groupby(['date'],as_index=False)['profit_loss'].sum()
    print(test)
    df_win_day=test.loc[test['profit_loss']>0,['date','profit_loss']]
    print(df_win_day)
    pie_chart = px.pie( df_win_day, values='profit_loss', names='date')
    pie_chart=pie_chart.to_html()
    return pie_chart