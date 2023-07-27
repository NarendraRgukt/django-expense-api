from rest_framework import serializers 
from expenses import models
from django.contrib.auth import get_user_model

class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email']


class ExpenseSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model=models.Expense
        exclude=("created_at","updated_at","created_by")


    def update(self,instance,validated_data):
        expense=super().update(instance,validated_data)
        return expense



class ExpenseSerializerRetrieve(serializers.ModelSerializer):
    created_by = UserSerializer1()

    class Meta:
        model=models.Expense
        fields=['id', 'created_by', 'name', 'date_of_expense', 'category', 'description', 'amount', 'created_at', 'updated_at']

