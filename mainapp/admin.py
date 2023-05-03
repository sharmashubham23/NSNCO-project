from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import *


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True

    class Meta:
        model = CustomUser
        fields = '__all__'


class EmployeeAdmin(UserAdmin):
    form = PostForm
    list_display = ('username', 'name', 'email', 'gender')


admin.site.register(CustomUser, EmployeeAdmin)
admin.site.register(Clienttable)
admin.site.register(workTable)
admin.site.register(artistTable)
