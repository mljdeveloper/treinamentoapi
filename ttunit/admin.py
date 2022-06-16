from django.contrib import admin
from .models import TTUnit

# Register your models here.


class TTUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'unittype', 'businessdate', 'username', 'price',
                    'modal', 'petpolicy')
    list_display_links = ('id', 'unittype')
    list_per_page = 200
    search_fields = ('id', 'unittype',)

    def get_queryset(self, request):
        qs = super(TTUnitAdmin, self).get_queryset(request)
        return qs.filter(username=request.user)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)


admin.site.register(TTUnit, TTUnitAdmin)
