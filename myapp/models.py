from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
import datetime

class Employee(models.Model):
    gender_choice = [
    ('M', 'Male'),
    ('F', 'Female'),
    ]

    marital_status = [
    ('M', 'Married'),
    ('UM', 'Unmarried'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True,blank=True)
    email = models.EmailField(max_length=50,unique=True, null=True,blank=True)
    employee_id = models.CharField(max_length=10, unique=True)
    date_of_joining = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=2,null=True, blank=True,choices=gender_choice)
    marital_status = models.CharField(max_length=2,null=True, blank=True,choices=marital_status)
    # department = models.CharField(max_length=50)
    # position = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    leave_balance=models.PositiveIntegerField(default=0)

    # first_name=models.CharField(max_length=15, null=True,blank=True)
    # last_name = models.CharField(max_length=15, null=True,blank=True)

    
    def __str__(self):
        return self.user.username






class HolidayList(models.Model):


    financial_year = models.CharField(max_length=10, choices= (('2023-2024', '2023-2024'),('2024-2025', '2024-2025')))
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_type = models.CharField(max_length=50, choices=(('fixed','fixed'),('optional','optional')))
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name + '-' + self.location
    
class FY(models.Model):
    financial_year = models.CharField(max_length=10, unique=True, primary_key=True)
    set_current = models.CharField(choices=(('YES', 'YES'),('NO', 'NO')), max_length=3)

    def __str__(self):
        return self.financial_year   


class LeaveRequest(models.Model):
    leave_type = [
    ('Sick leave', 'Sick leave'),
    ('Vacation leave', 'Vacation leave'),
    ('Travel leave', 'Travel leave'),
    ('Emergency leave', 'Emergency leave'),

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    leave_type = models.CharField(max_length=15,null=True, blank=True,choices=leave_type)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.start_date} to {self.end_date}"
    
class LeaveBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='leave_balance')
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Balance: {self.balance}"    
    