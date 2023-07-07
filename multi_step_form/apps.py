from django.apps import AppConfig


class MultiStepFormConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'multi_step_form'

    def ready(self):
        import multi_step_form.signals
        from django.db.models.signals import post_save
        from multi_step_form.signals import createBill, sendMail
        from multi_step_form.models import Bill, SubscriptionPlan
        post_save.connect(createBill, sender=SubscriptionPlan)
        post_save.connect(sendMail, sender=Bill)
