import django_filters

from .models import *

class TradeSheetFilter(django_filters.FilterSet):
    class Meta:
        model = TradeSheet
        fields = '__all__'