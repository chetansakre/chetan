
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreationForm, LeaveRequestForm
from .models import FY, Employee, HolidayList, LeaveBalance,  LeaveRequest
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail



# from django.core.handlers.wsgi import WSGIRequest
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User



# @login_required
# def register_employee(request):
#     if request.method == 'POST':
#         form = EmployeeCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Additional processing, if needed
#             return redirect('myapp/employee_registration_success.html')
#     else:
#         form = EmployeeCreationForm()
    
#     return render(request, 'myapp/register_employee.html', {'form': form})

# def employee_registration_success(request):
#     return render(request, 'myapp/employee_registration_success.html')

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'myapp/home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return render(request,'myapp/pass_not_same.html')
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'myapp/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'myapp/username_wrong.html')
    return render (request,'myapp/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')







def employee_list(request):
    
    emp = Employee.objects.all()
    context={
        'emps':emp
    }
    return render(request,'myapp/list_of_employee.html',context)

def employee_details(request,id):
    context = {}
    obj_emp = Employee.objects.get(employee_id=id)
    context['emp'] = obj_emp
    return render(request,'myapp/employee_detail.html',context)


def holiday_list_view(request):
    context = {
        'obj_holiday': HolidayList.objects.order_by('event_date').all(),
        'obj_fy': FY.objects.get(set_current='YES'),
    }
    return render(request, 'myapp/holiday_list.html', context)




@login_required(login_url='login')
def apply_leave(request):



        if request.method == 'POST':
            form = LeaveRequestForm(request.POST)
            date1 = datetime.strptime(request.POST.get('start_date'), "%Y-%m-%d")
            date2 = datetime.strptime(request.POST.get('end_date'), "%Y-%m-%d")

          
            if( date1 > date2):
                return render(request, 'myapp/date_not_valid.html')
            
            # days = (leave_request.end_date - leave_request.start_date).days + 1
            
            # if(leave_balance.balance <=0 or leave_balance.balance<days ):
            #       return render(request,'myapp/not_allow_to_applyleave.html')
            



            if form.is_valid():
                leave_request = form.save(commit=False)
                leave_request.user = request.user
                leave_request.save()
                return redirect('/list/')  
       
        else:
            form = LeaveRequestForm()
  
            context = {'form': form,
          
             }
        return render(request, 'myapp/apply_leave.html', context) 





def my_leave(request):
    # messages.success(request,"welcome!!!")
    leave_requests = LeaveRequest.objects.filter(user=request.user)
    context = {'leave_requests': leave_requests}
    return render(request, 'myapp/my_leave.html', context)

def leave_list(request):
     leave_requests = LeaveRequest.objects.filter(user=request.user)
     context = {'leave_requests': leave_requests}
     return render(request, 'myapp/leave_list.html', context)
 




@login_required(login_url='login')
def leave_balance(request):
      balance = LeaveBalance.objects.get(user=request.user) 
      
   
      return render(request, 'myapp/leave_balance.html',{'date_diff':balance})


@login_required(login_url='login')

def approve_leave(request, id):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        leave_request = LeaveRequest.objects.get(id=id)

        
        if request.user != leave_request.user:
            # Check if the logged-in user has the authority to approve the leave
            return redirect('/leave_list/')
        current_status=leave_request.status
        if(current_status == 'Approved'):
            return render(request,'myapp/leave_already_approved.html')


        leave_request.status = 'Approved'
        leave_balance = LeaveBalance.objects.get(user=leave_request.user)
        days = (leave_request.end_date - leave_request.start_date).days + 1



        if(leave_balance.balance <=0 or leave_balance.balance<days ):
            return render(request,'myapp/not_allow_to_applyleave.html')


        leave_request.save()
        # for u in LeaveRequest.objects.filter(status='Approved',user = request.user):
        #         send_mail(
        #             '!!! checklist reminder !!!',
        #             'Hi ,please complete your task',
        #             'employeeleave111@gmail.com',
        #             [user.email],
        #                                 )
        # Update leave balance
        leave_balance = LeaveBalance.objects.get(user=leave_request.user)
        leave_balance.balance -= (leave_request.end_date - leave_request.start_date).days + 1
        leave_balance.save()



    return redirect('/leave_list/')


@login_required(login_url='login')

def reject_leave(request, id):
    leave_request = LeaveRequest.objects.get(id=id)
    
    if request.user != leave_request.user:
        # Check if the logged-in user has the authority to reject the leave
        return redirect('/leave_list/')
    
    current_status=leave_request.status
    if(current_status == 'Approved'):

          leave_balance = LeaveBalance.objects.get(user=leave_request.user)
          
          leave_balance.balance += (leave_request.end_date - leave_request.start_date).days + 1
          leave_balance.save()

    if(current_status=='Rejected'):
        return render(request,'myapp/leave_already_rejected.html')




    leave_request.status = 'Rejected'
    leave_request.save()

    return redirect('/leave_list/')



