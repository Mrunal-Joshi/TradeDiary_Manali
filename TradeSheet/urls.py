from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.displaysheet, name="tradesheet"),
    path('edit/<int:id>',views.editTrade, name="editTrade"),
    path('delete/<int:id>',views.deleteTrade, name="deleteTrade")

]