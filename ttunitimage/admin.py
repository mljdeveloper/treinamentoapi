from django.contrib import admin
from .models import TTUnitImage

# Register your models here.


class TTUnitImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit', 'photo', 'description',
                    'create_at', 'updated_at')
    list_display_links = ('id', 'unit')
    list_per_page = 200
    search_fields = ('id', 'unit',)

    def get_queryset(self, request):
        qs = super(TTUnitImageAdmin, self).get_queryset(request)
        return qs.filter()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


admin.site.register(TTUnitImage, TTUnitImageAdmin)
