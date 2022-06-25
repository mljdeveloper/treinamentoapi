from django.contrib import admin
from .models import User, Plan


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username')
    list_per_page = 10
    search_fields = ('username',)


admin.site.register(User, UserAdmin)
admin.site.register(Plan)
