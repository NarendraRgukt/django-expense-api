from django.contrib import admin
from expenses import models

class ExpenseAdmin(admin.ModelAdmin):
    ordering=("created_by","name","date_of_expense","category","amount","description")
    list_display = ('name','created_by', 'date_of_expense', 'category', 'amount', 'created_at', 'updated_at')

admin.site.register(models.Expense, ExpenseAdmin)
