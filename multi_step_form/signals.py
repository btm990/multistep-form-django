from multi_step_form.welcome_email.index import htmlTemplate
from multi_step_form.models import Bill, SubscriptionPlan, User

from django.core.mail import send_mail
from django.conf import settings

from multi_step_form.serializers import BillSerializer, SubscriptionPlanSerializer, UserSerializer

PLANS_PRICING = {
"Arcade": {
    'Monthly': 9,
    'Yearly': 90
},
"Advanced": {
    'Monthly': 12,
    'Yearly': 120
},
"Pro": {
    'Monthly': 15,
    'Yearly': 150
}
}
ADDONS_PRICING = {
"Online_service": {
    'Monthly': 1,
    'Yearly': 10
},
"Larger_Storage": {
    'Monthly': 2,
    'Yearly': 20,
},
"Customizable_profile": {
    'Monthly': 2,
    'Yearly': 20
}
    }

def createBill(sender, instance, created, **kwargs):
    subscriptionObj = SubscriptionPlanSerializer(instance)

    if created:

        addons = {key : val for (key, val) in subscriptionObj.data.items() if key in [k for k in ADDONS_PRICING.keys()]}

        if subscriptionObj.data['yearly'] == "on":
            [OST, LST, CPT] = [ADDONS_PRICING[k]['Yearly'] if v == "on" else 0 for (k, v) in addons.items()]
            planPrice = PLANS_PRICING[subscriptionObj.data['plan']]['Yearly']
            bill = Bill(
                subscription=instance,
                Plan_Total=planPrice,
                Larger_Storage_Total=LST,
                Online_service_Total=OST,
                Customizable_Profile_Total=CPT,
                BillTotal = sum([planPrice, CPT, LST, OST])
            )
            bill.save()
            
        else:
            [OST, LST, CPT] = [ADDONS_PRICING[k]['Monthly'] if v == "on" else 0 for (k, v) in addons.items()]
            planPrice = PLANS_PRICING[subscriptionObj.data['plan']]['Monthly']
            bill = Bill(
                subscription=instance,
                Plan_Total= planPrice,
                Larger_Storage_Total=LST,
                Online_service_Total=OST,
                Customizable_Profile_Total=CPT,
                BillTotal = sum([planPrice, CPT, LST, OST])
            )
            bill.save()


def sendMail(sender, instance, created, **kwargs):
    if created:
        bill = BillSerializer(instance)
        subscriptionObj =  SubscriptionPlan.objects.get(id=bill.data['subscription'])
        subscription = SubscriptionPlanSerializer(subscriptionObj)
        userObj = User.objects.get(id=subscription.data['user'])
        user = UserSerializer(userObj)

        name = user.data['name'] if len(user.data['name'].split(" ")) == 1 else user.data['name'].split(" ")[0]
        plan = subscription.data['plan']
        planTotal = bill.data['Plan_Total']*18.80
        yearly = 'yearly' if subscription.data['yearly'] == 'on' else 'monthly'
        dateTime = " | ".join(subscription.data['created'].split(".")[0].split("T"))
        billTotal = bill.data['BillTotal']*18.80
        kwargs = {k : v for (k, v) in bill.data.items() if k not in ['id', 'subscription', 'Plan_Total', 'BillTotal', 'created']}

        html = htmlTemplate(name, plan, planTotal, yearly, dateTime, billTotal, **kwargs)
        subject = 'Your LoremGaming Subscription Confirmation'
        message = 'Glad to have you on board!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.data['email']],
            fail_silently=False,
            html_message=html
        )

