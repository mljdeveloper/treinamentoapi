from django.contrib import admin
from .models import CostCenter

# Register your models here.


class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'cost_center', 'name', 'create_at',
                    'updated_at', 'display', 'username')
    list_display_links = ('id', 'cost_center')
    list_per_page = 200
    search_fields = ('id', 'cost_center',)
    list_editable = ('display',)
    exclude = ['username', ]

    def get_queryset(self, request):
        qs = super(CostCenterAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(CostCenter, CostCenterAdmin)
