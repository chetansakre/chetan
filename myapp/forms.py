from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from .models import LeaveRequest
# from django.contrib.admin.widgets import AdminDateWidget




class EmployeeCreationForm(UserCreationForm):
    employee_id = forms.CharField(max_length=10)
    department = forms.CharField(max_length=50)
    position = forms.CharField(max_length=50)
    username = forms.CharField(max_length=15)
    first_name=forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=50)

    
    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'email', 'employee_id', 'department', 'position', 'password1', 'password2')
        # fields = '__all__'
        # exclude = ['userid']

class LeaveRequestForm(forms.ModelForm):
    # start_date = forms.SplitDateTimeField(widget=AdminDateWidget)
    # end_date = forms.SplitDateTimeField(widget=AdminDateWidget)


    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'leave_type']
        widgets={
            'start_date':forms.DateInput(attrs={'type': 'date'}),
            'end_date':forms.DateInput(attrs={'type': 'date'}),

           
            }
