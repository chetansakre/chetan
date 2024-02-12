from django.contrib import admin
# from .models import LeaveType
from .models import Employee
from .models import HolidayList
from .models import FY
from .models import LeaveRequest
from .models import LeaveBalance




# from .models import LeaveRequest


# Register your models here.
# admin.site.register(LeaveType)
# admin.site.register(LeaveRequest)
admin.site.register(Employee)
admin.site.register(HolidayList)
admin.site.register(FY)
admin.site.register(LeaveRequest)
admin.site.register(LeaveBalance)










