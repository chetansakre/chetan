from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import LeaveBalance

@receiver(post_save, sender=User)
def create_leave_balance(sender, instance, created, **kwargs):
    if created:
        LeaveBalance.objects.create(user=instance, balance=12)  # Set initial balance here

@receiver(post_save, sender=User)
def save_leave_balance(sender, instance, **kwargs):
    try:
        instance.leave_balance.save()  # 'leave_balance' is the related_name for the OneToOneField
    except LeaveBalance.DoesNotExist:
        LeaveBalance.objects.create(user=instance, balance=12)