from django.db import models
from django.contrib.auth import get_user_model

labels = (

    ('Health', 'Health'),
    ('Electronics', 'Electronics'),
    ('Travel', 'Travel'),
    ('Education', 'Education'),
    ('Books', 'Books'),
    ('Others', 'Others'),
)



class Expense(models.Model):
    created_by=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=140)
    date_of_expense=models.DateField()
    category=models.CharField(choices=labels,max_length=15)
    description=models.TextField()
    amount=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
