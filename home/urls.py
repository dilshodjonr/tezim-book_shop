from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('' , views.home , name="home"),

    # peference
    path("refereces" , views.refereces , name="references"),
    path("reference/create" , views.reference_create , name="reference_create"),
    path("reference/update/<int:pk>" ,views.reference_update , name="reference_update"),
    path("reference/delete/<int:pk>/", views.reference_delete, name="reference_delete"),

    # Staff
    path("staff" , views.staff_view , name="staff_view"),
    path("staff/create", views.staff_create , name="staff_create"),
    path("staff/update/<int:pk>" ,views.staff_update , name="staff_update"),
    path("staff/delete/<int:pk>/", views.staff_delete, name="staff_delete"),

    #Staff_Payment
    path("staff" , views.staff_view , name="staff_view"),    
    path("staff_payment/create", views.staff_payment_create , name="staff_payment_create"), 
    #Staff_work 
    path("staff_work/create", views.staff_work_create , name="staff_work_create"),    
    # Cost
    path("Cost" , views.cost_view,  name="cost_view"), 
    path("cost/create", views.cost_create , name="cost_create"),
    path("cost/update/<int:pk>" ,views.cost_update , name="cost_update"),
    path("cost/delete/<int:pk>/", views.cost_delete, name="cost_delete"),

    #book
    path("book/create", views.book_create , name="book_create"),
    path("book/update/<int:pk>" ,views.book_update , name="book_update"),
    path("book/delete/<int:pk>/", views.book_delete, name="book_delete"),

    #Sotuv
    path("Sotuv" , views.sotuv_view,  name="sotuv_view"),   
    path("sotuv/create", views.sotuv_create , name="sotuv_create"),
    path("sotuv/update/<int:pk>" ,views.sotuv_update , name="sotuv_update"),
    path("sotuv/delete/<int:pk>", views.sotuv_delete, name="sotuv_delete"),

    #chiqim
    path("chiqim" , views.chiqim_view,  name="chiqim_view"),
    path("chiqim/create", views.chiqim_create , name="chiqim_create"),
    path("chiqim/update/<int:pk>" ,views.chiqim_update , name="chiqim_update"),
    path("chiqim/delete/<int:pk>/", views.chiqim_delete, name="chiqim_delete"),
    #daromat
    path("daromad" , views.daromad_view,  name="daromad_view"),
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

         