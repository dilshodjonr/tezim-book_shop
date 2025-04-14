
from django.db.models.signals import post_delete , post_save
from django.dispatch import receiver
from .models import Cost, Book_model , Income , Staff_Payment , Staff , Staff_Work


@receiver([post_delete, post_save], sender=Cost)
@receiver([post_delete, post_save], sender=Income)
def signal_cost_quantity(sender, instance,  **kwargs):
    try:
        cost = Cost.objects.filter(name__name=instance.name, is_deleted=False)
        book = Book_model.objects.get(name=instance.name, is_deleted=False)
        income = Income.objects.filter(sold_book__name=instance.name, is_deleted=False)
    except:
        cost = Cost.objects.filter(name__name=instance.sold_book, is_deleted=False)
        book = Book_model.objects.get(name=instance.sold_book, is_deleted=False)
        income = Income.objects.filter(sold_book__name=instance.sold_book, is_deleted=False)

    cost_book_quantity = 0
    sold_book_quantity = 0


    for i in cost:
      cost_book_quantity += i.quantity

    
    for i in income:
      sold_book_quantity += i.quantity

    book.quantity = cost_book_quantity - sold_book_quantity

    book.save()



@receiver([post_delete, post_save], sender=Staff_Payment)
@receiver([post_delete, post_save], sender=Staff_Work)
def signal_cost_quantity(sender, instance,  **kwargs):
   staff = Staff.objects.get(pk=instance.staff.pk)
   staff_payment_list = Staff_Payment.objects.filter(staff=staff , is_deleted=False)
   staff_work_list = Staff_Work.objects.filter(staff=staff , is_deleted=False)

   total_payment = 0
   total_work = 0

   for payment in staff_payment_list:
      total_payment += payment.price

   for work in staff_work_list:
      total_work += work.price


   staff.balance = total_work - total_payment
   staff.save()