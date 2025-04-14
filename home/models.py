from django.db import models

# Create your models here.

class refrences(models.Model):
    name = models.CharField(verbose_name="refrences nomi", max_length=255)
    value = models.CharField(verbose_name="refrences qiymati", max_length=255)
    is_deleted = models.BooleanField(default=False, verbose_name="O'chirilganmi?")  # Soft delete flag
    created_at = models.DateField(verbose_name="Qo'shilgan sana", auto_now_add=True)  # Qo'shilgan vaqt

    def __str__(self):
        return f"{self.value}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True  # O'chirilgan sifatida belgilanadi
        self.save()  # O'zgarishlarni saqlash  



    
class Book_model(models.Model):
    name = models.CharField(max_length=225, verbose_name="Kitob nomi", unique=True)
    description = models.TextField(verbose_name="Kitob tavsifi")
    price = models.FloatField(verbose_name="Kitob narxi")
    quantity = models.IntegerField(verbose_name="Kitob soni")
    category = models.ForeignKey(
        refrences, 
        on_delete=models.SET_NULL,  # Refrences o‘chilganda category NULL bo‘ladi
        null=True, blank=True,
        verbose_name="Kitob turi", 
        related_name="books"
    )
    image = models.ImageField(upload_to="media", verbose_name="Mahsulot rasmi")
    created_at = models.DateField(verbose_name="Qo'shilgan sana", auto_now_add=True)
    is_deleted = models.BooleanField(default=False, verbose_name="O'chirilganmi?")  # Soft delete flag

    def __str__(self):
        return self.name


    def delete(self, *args, **kwargs):
        self.is_deleted = True  # O'chirilgan sifatida belgilanadi
        self.save()  # O'zgarishlarni saqlash


class Income(models.Model):
    sold_book = models.ForeignKey(Book_model, on_delete=models.CASCADE, verbose_name="Sotilgan kitob nomi")
    quantity = models.IntegerField(verbose_name="Sotilgan kitob soni")
    price = models.FloatField(verbose_name="Sotilgan kitob narxi")
    created_at = models.DateField(auto_now_add=True, verbose_name="Sotilgan kitob sanasi")
    is_deleted = models.BooleanField(default=False, verbose_name="O'chirilganmi?")  # Soft delete flag

    def __str__(self):
        return f"{self.sold_book}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True  # O'chirilgan sifatida belgilanadi
        self.save()  # O'zgarishlarni saqlash  



class Cost(models.Model):
    name = models.ForeignKey(Book_model, on_delete=models.CASCADE, verbose_name="Xarajat nomi", related_name="costs_as_name")
    price = models.FloatField(verbose_name="Xarajat narxi")
    description = models.TextField(verbose_name="Xarajat malumoti")
    quantity = models.IntegerField(verbose_name="Xarajat miqdori")
    created_at = models.DateField(auto_now_add=True, verbose_name="Xarajat sanasi")
    is_deleted = models.BooleanField(default=False, verbose_name="O'chirilganmi?")  # Soft delete flag

    def __str__(self):
        return f"{self.name}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True  # O'chirilgan sifatida belgilanadi
        self.save()  # O'zgarishlarni saqlash  



class Output(models.Model):
    name = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Chiqim nomi")
    price = models.FloatField(verbose_name="Chiqim narxi")
    description = models.TextField(verbose_name="Chiqim malumoti")
    created_at = models.DateField(auto_now_add=True, verbose_name="Chiqim sanasi")
    is_deleted = models.BooleanField(default=False, verbose_name="O'chirilganmi?")  # Soft delete flag

    def __str__(self):
        return f"{self.name}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True  # O'chirilgan sifatida belgilanadi
        self.save()  # O'zgarishlarni saqlash  



class Staff(models.Model):
    full_name = models.CharField(verbose_name="Xodimning to'liq ismi", max_length=255)
    gender = models.ForeignKey(refrences, on_delete=models.CASCADE, verbose_name="Xodimning jinsi")
    phone_number = models.TextField(verbose_name="Xodimning telefon raqami")
    birthday = models.DateField(verbose_name="Xodimning tug‘ilgan sanasi")
    is_deleted = models.BooleanField(default=False, verbose_name="O‘chirilganmi?")  # Soft delete flag
    created_at = models.DateField(verbose_name="Qo‘shilgan sana", auto_now_add=True)  # Qo‘shilgan vaqt
    balance = models.FloatField(default=0)
    def __str__(self):
        return f"{self.full_name}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True  # O‘chirilgan sifatida belgilanadi
        self.save()  # O‘zgarishlarni saqlash  



class Staff_Work(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Ishlagan xodim")
    price = models.FloatField(verbose_name="Ishlagan xodimning maoshi")
    time_work = models.FloatField(verbose_name="Ishlagan xodimning ish vaqti")
    created_at = models.DateField(auto_now_add=True, verbose_name="To‘lov sanasi")
    is_deleted = models.BooleanField(default=False, verbose_name="O‘chirilganmi?")  # Soft delete

    def __str__(self):
        return f"{self.staff} - {self.price} UZS"

    def delete(self, *args, **kwargs):
        """O‘chirish o‘rniga is_deleted=True qilib belgilaydi"""
        self.is_deleted = True
        self.save()
    
class Staff_Payment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Xodim")
    price = models.FloatField(verbose_name="To‘langan summa")
    created_at = models.DateField(auto_now_add=True, verbose_name="To‘lov sanasi")
    is_deleted = models.BooleanField(default=False, verbose_name="O‘chirilganmi?")  # Soft delete

    def __str__(self):
        return f"{self.staff} - {self.price} UZS"

    def delete(self, *args, **kwargs):
        """O‘chirish o‘rniga is_deleted=True qilib belgilaydi"""
        self.is_deleted = True
        self.save()
