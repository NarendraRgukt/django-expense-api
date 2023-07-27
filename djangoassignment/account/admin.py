from django.contrib import admin

from account import models

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('email','name','is_active','is_staff','is_superuser')
    fieldsets=(
        (None,{'fields':('email','name','password')}),
        ("Permission",{
            'fields':(
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
        ("Important Dates",{
            'fields':(
                'last_login',

            )
        }

        )
    )
    readonly_fields=['last_login']
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

admin.site.register(models.User,CustomUserAdmin)
