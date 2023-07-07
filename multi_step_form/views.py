from django.http import JsonResponse
from multi_step_form.models import User
from multi_step_form.models import SubscriptionPlan
from multi_step_form.serializers import SubscriptionPlanSerializer
from multi_step_form.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response({'users': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user' : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def user(request, id):
    if request.method == 'GET':
        data = User.objects.get(pk=id)
        serializer = UserSerializer(data)
        return Response({'user': serializer.data})
    
    elif request.method == 'POST':
        data = User.objects.get(pk=id)
        serializer = UserSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data = User.objects.get(pk=id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def subscriptions(request):
    if request.method == 'GET':
        data = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(data, many=True)
        return Response({'subscriptions': serializer.data})
    
    elif request.method == 'POST':
        serializer = SubscriptionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'subscription': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def subscription(request, user_id):
    if request.method == 'GET':
        data = SubscriptionPlan.objects.get(user=user_id)
        serializer = SubscriptionPlanSerializer(data)
        return Response({'subscription': serializer.data})
    
    elif request.method == 'POST':
        data = SubscriptionPlan.objects.get(user=user_id)
        serializer = SubscriptionPlanSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'subscription': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data = SubscriptionPlan.objects.get(user=user_id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
