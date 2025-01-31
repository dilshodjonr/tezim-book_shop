from django.db import models

# Create your models here.

class refrences(models.Model):
    name =  models.CharField(verbose_name="refrences nomi", max_length=255)
    value =  models.CharField(verbose_name="refrences qiymati", max_length=255)

    def __str__(self):
        return f"{self.value}"


class Book_model(models.Model):
    name = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Kitob nomi", related_name="books_as_name")
    description = models.TextField(verbose_name="Kitob tavsifi")
    price = models.FloatField(verbose_name="Kitob narxi")
    quantity = models.IntegerField(verbose_name="Kitob soni")
    category = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Kitob turi", related_name="books_as_category")
    image = models.ImageField(upload_to="media", verbose_name="Kitob rasmi")
    created_at = models.DateField(auto_now_add=True, verbose_name="Kitob qoshilgan sanasi")

    def __str__(self):
        return f"{self.name}"


class Income(models.Model):
    sold_book = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Sotilgan kitob nomi")
    quantity = models.IntegerField(verbose_name="Sotilgan kitob soni")
    price = models.FloatField(verbose_name="Sotilgan kitob narxi")
    created_at = models.DateField(auto_now_add=True, verbose_name="Sotilgan kitob sanasi")

    def __str__(self):
        return f"{self.sold_book}"


class Cost(models.Model):
    name = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Xarajat nomi", related_name="costs_as_name")
    price = models.FloatField(verbose_name="Xarajat narxi")
    category = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Xarajat turi", related_name="costs_as_category")
    description = models.TextField(verbose_name="Xarajat malumoti")
    quantity = models.IntegerField(verbose_name="Xarajat miqdori")
    created_at = models.DateField(auto_now_add=True, verbose_name="Xarajat sanasi")
    def __str__(self):
        return f"{self.name}"


class Output(models.Model):
    name = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Chiqim nomi")
    price = models.FloatField(verbose_name="Chiqim narxi")
    description = models.TextField(verbose_name="Chiqim malumoti")
    created_at = models.DateField(auto_now_add=True, verbose_name="Chiqim sanasi")

    def __str__(self):
        return f"{self.name}"


class Staff(models.Model):
    full_name = models.CharField(verbose_name="Xodimning tolig ismi", max_length=255)
    gender = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Xodimning jinsi")
    phone_number = models.TextField(verbose_name="Xodimning telefon raqami")
    birthday = models.DateField(verbose_name="Xodimning tugulgan sanasi")

    def __str__(self):
        return f"{self.full_name}"


class Staff_Work(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Ishlagan xodim")
    price = models.FloatField(verbose_name="Ishlagan xodimning maoshi")
    time_work = models.FloatField(verbose_name="Ishlagan xodimning ish vaqti")
    created_at = models.DateField(auto_now_add=True, verbose_name="tolov sanasi")

    def __str__(self):
        return f"{self.staff}"
    

class Staff_Payment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="xodim")
    price = models.FloatField(verbose_name="tolangan summa")
    created_at = models.DateField(auto_now_add=True, verbose_name="tolov sanasi")
    def __str__(self):
        return f"{self.staff}"
