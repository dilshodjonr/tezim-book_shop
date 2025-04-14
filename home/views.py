from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404

from .forms import *
from .models import *
# Create your views here.
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def home(request):
    # Barcha o'chirilmagan kitoblarni olish
    books = Book_model.objects.filter(is_deleted=False)  # faqat o'chirilmagan kitoblarni olish

    # Qidiruv parametrini olish
    search = request.GET.get('search', None)
    
    # Agar search bor bo'lsa, qidiruv natijasini filtrlash
    if search:
        books = books.filter(name__icontains=search)
    
    # Kitobni tiklash (id orqali kitobni olish)
    try:
        book_id = 1  # Buni o'zingizga mos ravishda o'zgartiring (masalan, URL'dan olish)
        book = Book_model.objects.get(id=book_id)
        book.is_deleted = False  # O'chirilganni tiklash
        book.save()  # O'zgarishlarni saqlash
    except Book_model.DoesNotExist:
        # Kitob topilmagan bo'lsa, xato xabarini ko'rsatish
        print("Kitob topilmadi")

    # Kitobni "delete" qilish
    try:
        book_id_to_delete = 2  # O'chirish uchun kitobning id sini kiriting
        book_to_delete = Book_model.objects.get(id=book_id_to_delete)
        book_to_delete.is_deleted = True  # O'chirilgan deb belgilash
        book_to_delete.save()  # O'zgarishlarni saqlash
    except Book_model.DoesNotExist:
        # Kitob topilmagan bo'lsa, xato xabarini ko'rsatish
        print("O'chirish uchun kitob topilmadi")
    
    # Context ga kitoblar va qidiruvni qo'shish
    context = {
        'books': books,
        'search': search  # Qidiruv so'rovini yuborish
    }

    return render(request, 'index.html', context=context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tiziga muxaviyatli kirdingiz")
            return redirect('home')
        else:
            messages.error(request, "Login yoki parol notogri")
    return render(request , 'login.html')



def logout_view(request):
    logout(request)
    messages.info(request, "Tizimdan chiqdinggiz")
    return redirect('login')


@login_required(login_url='login')
def refereces(request):
    referece_model = refrences.objects.filter(is_deleted=False)  # O'chirilmaganlarni olish
    referece_name = set()
    referece_values = dict()
    search = request.GET.get('search', None)  # Qidiruv parametri

    if search:
        referece_model = referece_model.filter(name__icontains=search)

    for item in referece_model:
        referece_name.add(item.name)
        for name in referece_name:
            if name == item.name:
                if name not in referece_values:
                    referece_values[name] = [{"id": item.id, "value": item.value}]
                else:
                    referece_values[name].append({"id": item.id, "value": item.value})  # Qiymatni qo'shish

    context = {
        "referece_values": referece_values,
        "search": search  # Qidiruv parametrini templatega yuborish
    }
    return render(request, "refereces.html", context=context)

@login_required(login_url='login')
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
@login_required(login_url='login')
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

@login_required(login_url='login')
def reference_delete(request , pk):
    refrence_item = refrences.objects.get(pk=pk)
    refrence_item.delete()
    return redirect('references')

# starr
@login_required(login_url='login')
def staff_view(request):
    staff_list = Staff.objects.filter(is_deleted=False)  # O'chirilmaganlarni olish
    staff_payment_list = Staff_Payment.objects.filter(is_deleted=False)
    work_list = Staff_Work.objects.filter(is_deleted=False)

    total_balance = 0

    for staff in staff_list:
        total_balance += staff.balance

    if total_balance == 0:
        int(total_balance)

    ism = request.GET.get('ism', None)
    jinsinitanlash = request.GET.get('jinsi', None)
    Telefon = request.GET.get("tel", None)

    if ism:
        staff_list = staff_list.filter(full_name__icontains=ism)
    if jinsinitanlash:
        staff_list = staff_list.filter(gender__value__icontains=jinsinitanlash)
    if Telefon:
        staff_list = staff_list.filter(phone_number__icontains=Telefon)

    context = {
        "staff_list": staff_list,
        "staff_payment_list": staff_payment_list,
        "work_list": work_list,
        "total_balance":total_balance
    }
    return render(request, "Staff/staff.html", context=context)

@login_required(login_url='login')
def staff_create(request):
    if request.method =="POST":
        forms = StaffForm(request. POST)
        if forms.is_valid():
            forms.save()
            return redirect("staff_view")
    else:
        forms = StaffForm()
    context = {
        "forms":forms
    }
    return render(request , "Staff/staff_create.html" , context=context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def staff_delete(request , pk):
    staff_item = Staff.objects.get(pk=pk)
    staff_item.delete()
    return redirect('staff_view')

# Cost
def cost_read(request, pk):
    cost = get_object_or_404(Cost, id=pk)  # Kitobni ID orqali olish
    return render(request, 'Cost/cost_korish.html', {'cost': cost})
  
@login_required(login_url='login')
def cost_view(request):
    cost_list = Cost.objects.filter(is_deleted=False)  # O'chirilmaganlarni olish

    search = request.GET.get('search', None)
    if search:
        cost_list = cost_list.filter(name__name__icontains=search)  # Kitob nomi bo‘yicha qidirish

    context = {
        "cost_list": cost_list
    }
    return render(request, "Cost/cost.html", context=context)


@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def cost_delete(request , pk):
    cost_item = Cost.objects.get(pk=pk)
    cost_item.delete()
    return redirect('cost_view')

# book create
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def book_delete(request , pk):
    book_item = Book_model.objects.get(pk=pk)
    book_item.delete()
    return redirect('home')

# Sotuv

@login_required(login_url='login')
def sotuv_view(request):
    sotuv_list = Income.objects.filter(is_deleted=False)  # O'chirilmaganlarni olish

    search = request.GET.get('search', None)
    if search:
        sotuv_list = sotuv_list.filter(sold_book__name__icontains=search)  # Kitob nomi bo‘yicha qidirish

    context = {
        "sotuv_list": sotuv_list
    }
    return render(request, "Sotuv/sotuv.html", context=context)


@login_required(login_url='login')
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

@login_required(login_url='login')
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
@login_required(login_url='login')
def sotuv_delete(request , pk):
    sotuv_item = Income.objects.get(pk=pk)
    sotuv_item.delete()
    return redirect('sotuv_view')

# chiqim
@login_required(login_url='login')
def chiqim_view(request):
    chiqim_list = Output.objects.filter(is_deleted=False)  # O'chirilmaganlarni olish

    search = request.GET.get('search', None)
    if search:
        chiqim_list = chiqim_list.filter(name__value__icontains=search)  # Chiqim nomi bo‘yicha qidirish

    context = {
        "chiqim_list": chiqim_list
    }
    return render(request, "chiqim/output.html", context=context)


@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def chiqim_delete(request , pk):
    chiqim_item = Output.objects.get(pk=pk)
    chiqim_item.delete()
    return redirect('chiqim_view')

#Daramat

from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import Cost, Output, Income, Staff_Payment
@login_required(login_url='login')
def daromad_view(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    # Sanalarni to'g'ri formatga o'tkazish
    start_date = parse_date(start_date) if start_date else None
    end_date = parse_date(end_date) if end_date else None

    # Agar foydalanuvchi sanalarni kiritgan bo'lsa, filtering qo‘llanadi
    cost_list = Cost.objects.filter()
    chiqim_list = Output.objects.filter()
    hodim_list = Income.objects.filter()
    payment_list = Staff_Payment.objects.filter()

    if start_date and end_date:
        cost_list = cost_list.filter(created_at__range=[start_date, end_date])
        chiqim_list = chiqim_list.filter(created_at__range=[start_date, end_date])
        hodim_list = hodim_list.filter(created_at__range=[start_date, end_date])
        payment_list = payment_list.filter(created_at__range=[start_date, end_date])

    total_cost_sum = sum(i.quantity * i.price for i in cost_list)
    total_chiqim_sum = sum(i.price for i in chiqim_list)
    total_hodim_sum = sum(i.quantity * i.price for i in hodim_list)
    total_payment_sum = sum(i.price for i in payment_list)

    profit = total_hodim_sum - (total_cost_sum + total_chiqim_sum + total_payment_sum)

    context = {
        "total_cost_sum": total_cost_sum,
        "total_chiqim_sum": total_chiqim_sum,
        "total_hodim_sum": total_hodim_sum,
        "total_payment_sum": total_payment_sum,
        "profit": profit,
        "start_date": start_date,
        "end_date": end_date,
    }
    return render(request, "Daromad/daromad.html", context=context)
@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def staff_work_update(request , pk):
    Staff_item = Staff_Work.objects.get(pk=pk)

    if request.method == "POST":
        forms = StaffWorkForm(request.POST , instance=Staff_item)
        if forms.is_valid():
            forms.save()
            return redirect('staff_view')
        
    forms = StaffWorkForm(instance=Staff_item)

    context = {
        "forms":forms
    }

    return render(request , 'Staff/staff_update.html' , context=context)
@login_required(login_url='login')
def staff_work_delete(request , pk):
    staff_item = Staff_Work.objects.get(pk=pk)
    staff_item.is_deleted = True
    staff_item.save()
    return redirect('staff_view')

@login_required(login_url='login')
def staff_payment_update(request , pk):
    Staff_item = Staff_Payment.objects.get(pk=pk)

    if request.method == "POST":
        forms = StaffpaymentForm(request.POST , instance=Staff_item)
        if forms.is_valid():
            forms.save()
            return redirect('staff_view')
        
    forms = StaffpaymentForm(instance=Staff_item)

    context = {
        "forms":forms
    }

    return render(request , 'Staff/staff_update.html' , context=context)

@login_required(login_url='login')
def staff_payment_delete(request , pk):
    staff_item = Staff_Payment.objects.get(pk=pk)
    staff_item.is_deleted=True
    staff_item.save()
    return redirect('staff_view')





def staff_payment_view(request):
    staff_payments = Staff_Payment.objects.filter(is_deleted=False)  # Faqat o‘chirilmaganlar

    search = request.GET.get('search', None)
    if search:
        staff_payments = staff_payments.filter(staff__full_name__icontains=search)

    context = {
        "staff_payments": staff_payments
    }
    return render(request, "staff/staff_payment.html", context=context)

def staff_work_view(request):
    staff_works = Staff_Work.objects.filter(is_deleted=False)  # Faqat o‘chirilmaganlar

    search = request.GET.get('search', None)
    if search:
        staff_works = staff_works.filter(staff__full_name__icontains=search)

    context = {
        "staff_works": staff_works
    }
    return render(request, "staff/staff_work.html", context=context)

from django.shortcuts import render, get_object_or_404


def book_detail(request, id):
    book = get_object_or_404(Book_model, id=id)  # Kitobni ID orqali topamiz
    return render(request, 'book/book_detail.html', {'book': book})  # Sahifaga jo'natamiz

def chiqim_read(request, pk):
    chiqim = get_object_or_404(Output, id=pk)  # Kitobni ID orqali olish
    return render(request, 'chiqim/chiqim_korish.html', {'chiqim': chiqim})

def sotuv_read(request, pk):
    sotuv = get_object_or_404(Income, id=pk)  # Kitobni ID orqali olish
    return render(request, 'Sotuv/sotuv_korish.html', {'sotuv': sotuv})

def staff_read(request, pk):
    staff = get_object_or_404(Staff, id=pk)  # Kitobni ID orqali olish
    return render(request, 'Staff/staff_korish.html', {'staff': staff})