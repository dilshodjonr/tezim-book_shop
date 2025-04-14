from django import forms
from .models import refrences , Staff , Cost , Book_model , Income , Output , Staff_Payment , Staff_Work

from django import forms
from .models import Income, Book_model  # To'g'ri import qiling

from django import forms
from .models import refrences

class refrencesForm(forms.ModelForm):
    
    NAME_CHOICES = [
        ('Kitob turi', 'Kitob turi'),
        ('Jinsi', 'Jinsi'),
        ('Chiqim nomi', ' Chiqim nomi'),
    ]

    name = forms.ChoiceField(
        choices=NAME_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = refrences
        fields = ["name", "value"]

        widgets = {
            "value": forms.TextInput(attrs={"class": "form-control"}),
        }

class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ["full_name", "gender" , "phone_number" , "birthday"]

        widgets = {
            "full_name":forms.TextInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control"}),
            "birthday":forms.DateInput(attrs={"class":"form-control" , "type":"date"}),           
        }

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['gender'].queryset = refrences.objects.filter(name="Jinsi")


    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if len(full_name) <= 2:
            raise forms.ValidationError("Xodimning ismi juda qisqa")
        return full_name
    

class StaffpaymentForm(forms.ModelForm):

    class Meta:
        model = Staff_Payment
        fields = ["staff", "price"]

        widgets = {
            "staff":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),           
        }

    
class CostForm(forms.ModelForm):

    class Meta:
        model = Cost
        fields = ["name", "price"  , "description", "quantity"]

        widgets = {
            "name":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "quantity": forms.NumberInput(attrs={"class":"form-control"}),
                    
        }

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book_model
        fields = ['name' , 'description' , 'price' , 'category' , 'image' ,]

        widgets = {
             "name":forms.TextInput(attrs={"class":"form-control"}),
             "description":forms.Textarea(attrs={"class":"form-control"}),
             "price":forms.NumberInput(attrs={"class":"form-control"}),
             "category":forms.Select(attrs={"class":"form-control"}),
             "image":forms.ClearableFileInput(attrs={"class":"form-control"}),
        }


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].queryset = refrences.objects.filter(name="Kitob nomi")
        self.fields['category'].queryset = refrences.objects.filter(name="Kitob turi")



    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 2:
            raise forms.ValidationError("Kitob nomi juda qisqa")
        return name


class SotuvForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ["sold_book", "quantity", "price"]

        widgets = {
            "sold_book": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Faqat omborda mavjud kitoblarni chiqarish
        self.fields["sold_book"].queryset = Book_model.objects.filter(quantity__gt=0)

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        sold_book = self.cleaned_data.get("sold_book")

        if not sold_book:  # Agar hech qanday kitob tanlanmagan bo‘lsa
            raise forms.ValidationError("Iltimos, kitobni tanlang!")

        if not quantity or quantity <= 0:  # Agar miqdor noto‘g‘ri bo‘lsa
            raise forms.ValidationError("Miqdor 1 dan katta bo‘lishi kerak!")

        if quantity > sold_book.quantity:  # Mavjud kitob sonidan ko‘p bo‘lsa
            raise forms.ValidationError(f"Sizga kitob yetarli emas. Mavjud: {sold_book.quantity} dona")

        return quantity
        

class ChiqimForm(forms.ModelForm): 

    class Meta:
        model = Output
        fields = ["name", "description", "price"]

        widgets = {
            "name":forms.Select(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),       
        }

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].queryset = refrences.objects.filter(name="Chiqim nomi")

class StaffWorkForm(forms.ModelForm):
    class Meta:
        model = Staff_Work
        fields = ["staff", "price", "time_work"]

        widgets = {
            "staff":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "time_work":forms.NumberInput(attrs={"class": "form-control"}),
        }



   
    