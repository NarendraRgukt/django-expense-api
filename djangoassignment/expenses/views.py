from django.shortcuts import render
from expenses.models import Expense

from expenses import serializers
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView,GenericAPIView,RetrieveAPIView

from rest_framework import permissions 
from rest_framework import authentication 
from rest_framework import status
from rest_framework.response import Response
from expenses.permissions import ExpenseUpdatePermission


class ExpenseCreate(CreateAPIView):
    serializer_class=serializers.ExpenseSerializerCreate
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)



class ExpenseRetrieval(GenericAPIView):
    serializer_class = serializers.ExpenseSerializerRetrieve
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Expense.objects.all()
        else:
            return Expense.objects.filter(created_by=self.request.user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





class ExpenseUpdate(UpdateAPIView):
    serializer_class=serializers.ExpenseSerializerCreate
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated,ExpenseUpdatePermission]

    def get_queryset(self):

        return Expense.objects.filter(created_by=self.request.user)

class ExpenseDelete(DestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated,ExpenseUpdatePermission]
    queryset=Expense.objects.all()
    serializer_class=serializers.ExpenseSerializerCreate
    def get_queryset(self):
        return Expense.objects.filter(created_by=self.request.user)
    
    def destroy(self,*args,**kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)




    


        


        
