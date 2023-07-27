from django.urls import path
from expenses import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router=DefaultRouter()


app_name="expenses"

urlpatterns=[
    path("create/expense/",views.ExpenseCreate.as_view(),name="create-expense"),
    path("get/expenses/",views.ExpenseRetrieval.as_view(),name="retrieve-expenses"),
    path("update/expense/<int:pk>/",views.ExpenseUpdate.as_view(),name="update-expense"),
    path('delete/expense/<int:pk>/',views.ExpenseDelete.as_view(),name="expense-delete"),
    path('get/expense/detail/<int:pk>/',views.ExpenseRetrievalDetail.as_view(),name="expense-detail")
    

]