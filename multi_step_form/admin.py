from django.contrib import admin
from multi_step_form.models import Bill, User
from multi_step_form.models import SubscriptionPlan

admin.site.register(User)
admin.site.register(SubscriptionPlan)
admin.site.register(Bill)
