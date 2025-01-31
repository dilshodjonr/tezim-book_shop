from django import forms
from .models import refrences , Staff , Cost , Book_model , Income , Output , Staff_Payment , Staff_Work

class refrencesForm(forms.ModelForm):
    
    class Meta:
        model = refrences
        fields = ["name" , "value"]

        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "value":forms.TextInput(attrs={"class":"form-control"}),
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
        fields = ["name", "price" , "category" , "description", "quantity"]

        widgets = {
            "name":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "quantity": forms.NumberInput(attrs={"class":"form-control"}),
                    
        }

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].queryset = refrences.objects.filter(name="Kitob nomi")
        self.fields['category'].queryset = refrences.objects.filter(name="Kitob turi")

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book_model
        fields = ['name' , 'description' , 'price' , 'category' , 'image' ,]

        widgets = {
             "name":forms.Select(attrs={"class":"form-control"}),
             "description":forms.Textarea(attrs={"class":"form-control"}),
             "price":forms.NumberInput(attrs={"class":"form-control"}),
             "category":forms.Select(attrs={"class":"form-control"}),
             "image":forms.ClearableFileInput(attrs={"class":"form-control"}),
        }


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].queryset = refrences.objects.filter(name="Kitob nomi")
        self.fields['category'].queryset = refrences.objects.filter(name="Kitob turi")


class SotuvForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ["sold_book", "quantity" , "price" ]

        widgets = {
            "sold_book":forms.Select(attrs={"class":"form-control"}),
            "quantity":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
                    
        }

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['sold_book'].queryset = refrences.objects.filter(name="Kitob nomi")

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