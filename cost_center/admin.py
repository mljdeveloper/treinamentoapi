from django.contrib import admin
from .models import CostCenter

# Register your models here.


class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'costcenter', 'name', 'create_at',
                    'updated_at', 'display', 'username')
    list_display_links = ('id', 'costcenter')
    list_per_page = 200
    search_fields = ('id', 'costcenter',)
    list_editable = ('display',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(CostCenterAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(CostCenter, CostCenterAdmin)
