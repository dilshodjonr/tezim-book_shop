from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404

from .forms import refrencesForm
from .models import refrences , Book_model
from .models import Staff
from .forms import StaffForm , CostForm , BookForm , SotuvForm , ChiqimForm , StaffpaymentForm , StaffWorkForm
from .models import Cost, Book_model , Income , Output, Staff_Payment , Staff_Work
# Create your views here.

def home(request):
    books = Book_model.objects.all()
    context = {
        "books":books
    }
    return render(request, "index.html", context=context)
    


def refereces(request):
    referece_model = refrences.objects.all()
    referece_name = set()
    referece_values = dict()

    for item in referece_model:
        referece_name.add(item.name)
        for name in referece_name:
            if name == item.name:
                if name not in referece_values:
                    referece_values[name] = [{"id":item.id , "value":item.value}] 
                else:
                    referece_values[name].append({"id":item.id , "value":item.value})  # Qiymatni qo'shish

    print(referece_values)
    context = {
        "referece_values":referece_values
    }
    return render(request, "refereces.html", context=context)

def reference_create(request):
    if request.method == "POST":
        forms = refrencesForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("references")
    forms = refrencesForm()
    context = {
        "forms":forms
    }
    return render(request , "reference_create.html" , context=context)

def reference_update(request , pk):
    reference_item = refrences.objects.get(pk=pk)
    print("keldi")

    if request.method == "POST":
        forms = refrencesForm(request.POST , instance=reference_item)
        if forms.is_valid():
            forms.save()
            return redirect('references')
        
    forms = refrencesForm(instance=reference_item)

    context = {
        "forms":forms
    }

    return render(request , 'reference_update.html' , context=context)


def reference_delete(request , pk):
    refrence_item = refrences.objects.get(pk=pk)
    refrence_item.delete()
    return redirect('references')

# starr

def staff_view(request):
    staff_list = Staff.objects.all()
    staff_payment_list = Staff_Payment.objects.all()
    context = {
        "staff_list": staff_list,
        "staff_payment_list":staff_payment_list
    }
    return render(request, "Staff/staff.html" , context=context)

def staff_create(request):
    if request.method =="POST":
        forms = StaffForm(request. POST)
        if forms.is_valid():
            forms.save()
            return redirect("staff_view")
    forms = StaffForm()
    context = {
        "forms":forms
    }
    return render(request , "Staff/staff_create.html" , context=context)


def staff_update(request , pk):
    Staff_item = Staff.objects.get(pk=pk)

    if request.method == "POST":
        forms = StaffForm(request.POST , instance=Staff_item)
        if forms.is_valid():
            forms.save()
            return redirect('staff_view')
        
    forms = StaffForm(instance=Staff_item)

    context = {
        "forms":forms
    }

    return render(request , 'Staff/staff_update.html' , context=context)


def staff_delete(request , pk):
    staff_item = Staff.objects.get(pk=pk)
    staff_item.delete()
    return redirect('staff_view')

# Cost


def cost_view(request):
    cost_list = Cost.objects.all()
    context = {
        "cost_list": cost_list
    }
    return render(request, "Cost/cost.html" , context=context)



def cost_create(request):
    if request.method == "POST":
        forms = CostForm(request.POST)
        if forms.is_valid():
            cost = forms.save(commit=False)
            cost.save()
            return redirect("cost_view")
    else:
        forms = CostForm()

    context = {
        "forms": forms
    }

    return render(request, "Cost/cost_create.html", context=context)


def cost_update(request , pk):
    Cost_item = Cost.objects.get(pk=pk)

    if request.method == "POST":
        forms = CostForm(request.POST , instance=Cost_item)
        if forms.is_valid():
            forms.save()
            return redirect('cost_view')
        
    forms = CostForm(instance=Cost_item)

    context = {
        "forms":forms
    }

    return render(request , 'Cost/cost_update.html' , context=context)

def cost_delete(request , pk):
    cost_item = Cost.objects.get(pk=pk)
    cost_item.delete()
    return redirect('cost_view')

# book create

def book_create(request):
    if request.method =="POST":
        forms = BookForm(request.POST, request.FILES)
        if forms.is_valid():
            book = forms.save(commit=False)  
            book.quantity = 0 
            forms.save()
            return redirect("home")
    else:
        forms = BookForm()
    context = {
        "forms":forms
    }
    return render(request , "book/book_create.html" , context=context)

def book_update(request , pk):
    book_item = Book_model.objects.get(pk=pk)

    if request.method == "POST":
        forms = BookForm(request.POST , request.FILES , instance=book_item)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        
    forms = BookForm(instance=book_item)

    context = {
        "forms":forms
    }

    return render(request , 'book/book_update.html' , context=context)

def book_delete(request , pk):
    book_item = Book_model.objects.get(pk=pk)
    book_item.delete()
    return redirect('home')

# Sotuv


def sotuv_view(request):
    sotuv_list = Income.objects.all()
    context = {
        "sotuv_list": sotuv_list
    }
    return render(request, "Sotuv/sotuv.html" , context=context)


def sotuv_create(request):
    if request.method == "POST":
        forms = SotuvForm(request.POST)
        if forms.is_valid():
            sotuv = forms.save(commit=False)
            sotuv.save()
            return redirect("sotuv_view")
    else:
        forms = SotuvForm()

    context = {
        "forms": forms
    }

    return render(request, "Sotuv/sotuv_create.html", context=context)


def sotuv_update(request , pk):
    Sotuv_item = Income.objects.get(pk=pk)

    if request.method == "POST":
        forms = SotuvForm(request.POST , instance=Sotuv_item)
        if forms.is_valid():
            forms.save()
            return redirect('sotuv_view')
        
    forms = SotuvForm(instance=Sotuv_item)

    context = {
        "forms":forms
    }

    return render(request , 'Sotuv/sotuv_update.html' , context=context)

def sotuv_delete(request , pk):
    sotuv_item = Income.objects.get(pk=pk)
    sotuv_item.delete()
    return redirect('sotuv_view')

# chiqim

def chiqim_view(request):
    chiqim_list = Output.objects.all()
    context = {
        "chiqim_list": chiqim_list
    }
    return render(request, "chiqim/output.html" , context=context)

def chiqim_create(request):
    if request.method == "POST":
        forms = ChiqimForm(request.POST)
        if forms.is_valid():
            chiqim = forms.save(commit=False)
            chiqim.save()
            return redirect("chiqim_view")
    else:
        forms = ChiqimForm()

    context = {
        "forms": forms
    }

    return render(request, "chiqim/output_create.html", context=context)

def chiqim_update(request , pk):
    Chiqim_item = Output.objects.get(pk=pk)

    if request.method == "POST":
        forms = ChiqimForm(request.POST , instance=Chiqim_item)
        if forms.is_valid():
            forms.save()
            return redirect('chiqim_view')
        
    forms = ChiqimForm(instance=Chiqim_item)

    context = {
        "forms":forms
    }

    return render(request , 'chiqim/output_update.html' , context=context)

def chiqim_delete(request , pk):
    chiqim_item = Output.objects.get(pk=pk)
    chiqim_item.delete()
    return redirect('chiqim_view')

#Daramat

def daromad_view(request):
    cost_list = Cost.objects.all()
    chiqim_list = Output.objects.all()
    hodim_list = Income.objects.all()
    payment_list = Staff_Payment.objects.all()

    total_cost_sum = sum(i.quantity * i.price for i in cost_list)
    total_chiqim_sum = sum(i.price for i in chiqim_list)
    total_hodim_sum = sum(i.quantity * i.price for i in hodim_list)
    total_payment_sum = sum(i.price for i in payment_list)

    profit = total_hodim_sum - (total_cost_sum+total_chiqim_sum+total_payment_sum)

    context = {
        "total_cost_sum":total_cost_sum,
        "total_chiqim_sum":total_chiqim_sum,
        "total_hodim_sum":total_hodim_sum,
        "total_payment_sum":total_payment_sum,
        "profit":profit
    }
    return render(request, "Daromad/daromad.html" , context=context)
def staff_payment_create(request):
    if request.method =="POST":
        forms = StaffpaymentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("staff_view")
    forms = StaffpaymentForm()
    context = {
        "forms":forms
    }
    return render(request , "staff_payment/staff_payment_create.html" , context=context)


def staff_work_create(request):
    if request.method =="POST":
        forms = StaffWorkForm(request. POST)
        if forms.is_valid():
            forms.save()
            return redirect("staff_view")
    forms = StaffWorkForm()
    context = {
        "forms":forms
    }
    return render(request , "staff_work/staff_work_create.html" , context=context)
