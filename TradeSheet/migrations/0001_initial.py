# Generated by Django 3.2 on 2022-11-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('symbol', models.CharField(max_length=8)),
                ('no_of_shares', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Trading Sheet',
                'verbose_name_plural': 's',
            },
        ),
    ]