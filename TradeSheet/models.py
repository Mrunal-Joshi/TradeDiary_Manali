from django.db import models
from datetime import datetime
# Create your models here.

class TradeSheet(models.Model):   

    date = models.DateField(auto_now=False, auto_now_add=False,blank=True,default=datetime.now)
    symbol = models.CharField(max_length=8)
    no_of_shares = models.IntegerField(default=0)
    buy_price = models.FloatField(default=0)
    sell_price = models.FloatField(default=0)
    profit_loss = models.FloatField(default=0)

    class Meta:
        verbose_name = ("Trading Sheet")
    

    def __str__(self):
        """Every element will be stored as object , Therefore returning the name you want to display"""
        return self.symbol

    def get_absolute_url(self):
        """avoid hard coding paths in your templates. The reason for this is that paths might change, 
        and it will be a hassle to go through all your HTML and templates to 
        find every single URL or path and update it manually. It makes your code much harder to maintain.
        <!-- Bad --> <a href="/language/category/product/{{product.pk}}">Link</a>
        <!-- Good --><a href="{{product.get_absolute_url}}">Link</a>"""
        return reverse("_detail", kwargs={"pk": self.pk})

