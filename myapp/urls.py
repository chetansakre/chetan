from django.urls import path,include
from . import views

# app_name="myapp"

urlpatterns = [

    path('employee_list/', views.employee_list, name='employee_list'),
    path('<int:id>/details/', views.employee_details, name='employee_detail'),
    path('holiday_list/', views.holiday_list_view, name='holiday_list'),
    path('apply/', views.apply_leave, name='apply_leave'),
    path('list/', views.my_leave, name='leave_list'),
    path('leave_list/', views.leave_list, name='leave_list'),
    path('leave_balance/', views.leave_balance, name='leave_balance'),
     path('approve/<int:id>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:id>/', views.reject_leave, name='reject_leave'), 





    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    # path('employee/',include('myapp.urls')),



]
