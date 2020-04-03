from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import *
from .models import *

class UserAdmin(BaseUserAdmin):   # har nami mitune dashte bashe
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'full_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (   # in baraye userchange yani form avali
        (None, {'fields': ('full_name', 'email', 'password')}),
        ('personal_info', {'fields': ('is_active',)}),
        ('persmission', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (   # in baraye form dovomi user create
        (None, {'fields': ('full_name', 'email', 'password1', 'password2')}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()   # hamun dastresias ke bayad khali bashe


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)   # inam ke midunim