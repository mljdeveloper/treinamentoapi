from django.contrib import admin
from .models import TTCompany

# Register your models here.


class TTCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'codearea', 'phone', 'create_at',
                    'updated_at', 'username')
    list_display_links = ('id', 'contact')
    list_per_page = 200
    search_fields = ('id', 'contact',)

    def get_queryset(self, request):
        qs = super(TTCompanyAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(TTCompany, TTCompanyAdmin)
