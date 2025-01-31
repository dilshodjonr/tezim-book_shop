
from django.db.models.signals import post_delete , post_save
from django.dispatch import receiver
from .models import Cost, Book_model , Income


@receiver([post_delete, post_save], sender=Cost)
@receiver([post_delete, post_save], sender=Income)
def signal_cost_quantity(sender, instance,  **kwargs):
    try:
        cost = Cost.objects.filter(name__value=instance.name)
        book = Book_model.objects.get(name__value=instance.name)
        income = Income.objects.filter(sold_book__value=instance.name)
    except:
        cost = Cost.objects.filter(name__value=instance.sold_book)
        book = Book_model.objects.get(name__value=instance.sold_book)
        income = Income.objects.filter(sold_book__value=instance.sold_book)

    cost_book_quantity = 0
    sold_book_quantity = 0


    for i in cost:
      cost_book_quantity += i.quantity

    
    for i in income:
      sold_book_quantity += i.quantity

    book.quantity = cost_book_quantity - sold_book_quantity

    book.save()