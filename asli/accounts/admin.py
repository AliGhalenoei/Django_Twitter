from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
# .imports...
from .models import *
from .forms import *

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCrationForm

    fieldsets=(
        (None,{'fields':('email','username','password','img' , 'bio')}),
        ('Permissions',{'fields':('is_admin','is_active','last_login')}),

    )

    add_fieldsets=(
        (None,{'fields':('email','username','password','password2','img','bio')}),
    )

    list_display=('username','email','is_admin')
    list_filter=('is_active',)
    search_fields=('username',)
    filter_horizontal=()
    ordering=('username','email')

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)

admin.site.register(UserFollw_UnFollw)