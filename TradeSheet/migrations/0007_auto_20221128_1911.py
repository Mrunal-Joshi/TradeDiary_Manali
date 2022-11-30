# Generated by Django 3.2 on 2022-11-28 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TradeSheet', '0006_auto_20221126_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradesheet',
            name='buy_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tradesheet',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tradesheet',
            name='no_of_shares',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tradesheet',
            name='profit_loss',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tradesheet',
            name='sell_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tradesheet',
            name='symbol',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]