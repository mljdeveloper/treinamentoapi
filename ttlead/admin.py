from django.contrib import admin
from .models import TTlead

# Register your models here.


class TTLeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'codearea', 'sentemail', 'phone', 'create_at',
                    'unit',)
    list_display_links = ('id', 'first_name')
    list_per_page = 200
    search_fields = ('id', 'first_name',)

    def get_queryset(self, request):
        qs = super(TTLeadAdmin, self).get_queryset(request)
        return qs.filter()

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(TTlead, TTLeadAdmin)
