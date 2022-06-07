from django.contrib import admin
from .models import TTowner

# Register your models here.


class TTownerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'zipcode',
                    'username')
    list_display_links = ('id', 'first_name')
    list_per_page = 200
    search_fields = ('id', 'first_name',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(TTownerAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(TTowner, TTownerAdmin)
