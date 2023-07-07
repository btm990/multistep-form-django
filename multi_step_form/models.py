from django.db import models
import uuid


class User(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class SubscriptionPlan(models.Model):
    PLAN_TIER = (
        ('Arcade', 'Arcade'),
        ('Pro', 'Pro'),
        ('Advanced', 'Advanced'),
    )
    PERIOD_CHOICE = (
        ('on', 'yearly'),
        ('off', 'monthly')
    )
    ADDON_CHOICE = (
        ('on', 'on'),
        ('off', 'off')
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    plan = models.CharField(max_length=200, choices=PLAN_TIER)
    yearly = models.CharField(max_length=200, choices=PERIOD_CHOICE)
    Online_service = models.CharField(max_length=200, choices=ADDON_CHOICE, default="off")
    Larger_Storage = models.CharField(max_length=200, choices=ADDON_CHOICE, default="off")
    Customizable_profile = models.CharField(max_length=200, choices=ADDON_CHOICE, default="off")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user.email)

    
class Bill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    subscription = models.OneToOneField(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    Plan_Total = models.IntegerField(blank=True)
    Larger_Storage_Total = models.IntegerField(blank=True)
    Online_service_Total = models.IntegerField(blank=True)
    Customizable_Profile_Total = models.IntegerField(blank=True)
    BillTotal = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

